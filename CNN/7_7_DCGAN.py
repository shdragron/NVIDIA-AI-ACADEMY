import numpy as np
import tensorflow as tf
from keras import layers, models, callbacks, losses, utils, metrics, optimizers
import matplotlib.pyplot as plt


def display(images, n=10, size=(20, 3), cmap="gray_r", as_type="float32", save_to=None):
    if images.max() > 1.0:
        images = images / 255.0
    elif images.min() < 0.0:
        images = (images + 1.0) / 2.0

    plt.figure(figsize=size)
    for i in range(n):
        _ = plt.subplot(1, n, i + 1)
        plt.imshow(images[i].astype(as_type), cmap=cmap)
        plt.axis("off")

    if save_to:
        plt.savefig(save_to)
        print(f"\nSaved to {save_to}")

    plt.show()


def sample_batch(dataset):
    batch = dataset.take(1).get_single_element()
    if isinstance(batch, tuple):
        batch = batch[0]
    return batch.numpy()


def preprocess(img):
    # -1 ~ 1
    img = (tf.cast(img, "float32") - 127.5) / 127.5
    return img


IMAGE_SIZE = 64
CHANNELS = 1
BATCH_SIZE = 128
Z_DIM = 100
NOISE_PARAM = 0.1


def make_discriminator():
    discriminator_input = layers.Input(shape=(IMAGE_SIZE, IMAGE_SIZE, CHANNELS))
    x = layers.Conv2D(64, kernel_size=4, strides=2, padding="same", use_bias=False)(discriminator_input)
    x = layers.LeakyReLU(0.2)(x)
    x = layers.Dropout(0.3)(x)

    x = layers.Conv2D(128, kernel_size=4, strides=2, padding="same", use_bias=False)(x)
    x = layers.BatchNormalization(momentum=0.9)(x)
    x = layers.LeakyReLU(0.2)(x)
    x = layers.Dropout(0.3)(x)

    x = layers.Conv2D(256, kernel_size=4, strides=2, padding="same", use_bias=False)(x)
    x = layers.BatchNormalization(momentum=0.9)(x)
    x = layers.LeakyReLU(0.2)(x)
    x = layers.Dropout(0.3)(x)

    x = layers.Conv2D(512, kernel_size=4, strides=2, padding="same", use_bias=False)(x)
    x = layers.BatchNormalization(momentum=0.9)(x)
    x = layers.LeakyReLU(0.2)(x)
    x = layers.Dropout(0.3)(x)

    x = layers.Conv2D(1, kernel_size=4, strides=1, padding="valid", use_bias=False, activation="sigmoid")(x)
    discriminator_output = layers.Flatten()(x)

    discriminator = models.Model(discriminator_input, discriminator_output)
    # discriminator.summary()

    return discriminator


def make_generator():
    generator_input = layers.Input(shape=(Z_DIM,))
    x = layers.Reshape((1, 1, Z_DIM))(generator_input)

    x = layers.Conv2DTranspose(512, kernel_size=4, strides=1, padding="valid", use_bias=False)(x)
    x = layers.BatchNormalization(momentum=0.9)(x)
    x = layers.LeakyReLU(0.2)(x)

    x = layers.Conv2DTranspose(256, kernel_size=4, strides=2, padding="same", use_bias=False)(x)
    x = layers.BatchNormalization(momentum=0.9)(x)
    x = layers.LeakyReLU(0.2)(x)

    x = layers.Conv2DTranspose(128, kernel_size=4, strides=2, padding="same", use_bias=False)(x)
    x = layers.BatchNormalization(momentum=0.9)(x)
    x = layers.LeakyReLU(0.2)(x)

    x = layers.Conv2DTranspose(64, kernel_size=4, strides=2, padding="same", use_bias=False)(x)
    x = layers.BatchNormalization(momentum=0.9)(x)
    x = layers.LeakyReLU(0.2)(x)

    generator_output = layers.Conv2DTranspose(CHANNELS, kernel_size=4, strides=2, padding="same", use_bias=False, activation="tanh")(x)
    generator = models.Model(generator_input, generator_output)
    # generator.summary()

    return generator


class DCGAN(models.Model):
    def __init__(self, discriminator, generator, latent_dim):
        super(DCGAN, self).__init__()
        self.discriminator = discriminator
        self.generator = generator
        self.latent_dim = latent_dim

    def compile(self, d_optimizer, g_optimizer):
        super(DCGAN, self).compile()
        self.loss_fn = losses.BinaryCrossentropy()
        self.d_optimizer = d_optimizer
        self.g_optimizer = g_optimizer
        self.d_loss_metric = metrics.Mean(name="d_loss")
        self.d_real_acc_metric = metrics.BinaryAccuracy(name="d_real_acc")
        self.d_fake_acc_metric = metrics.BinaryAccuracy(name="d_fake_acc")
        self.d_acc_metric = metrics.BinaryAccuracy(name="d_acc")
        self.g_loss_metric = metrics.Mean(name="g_loss")
        self.g_acc_metric = metrics.BinaryAccuracy(name="g_acc")

    @property
    def metrics(self):
        return [
            self.d_loss_metric,
            self.d_real_acc_metric,
            self.d_fake_acc_metric,
            self.d_acc_metric,
            self.g_loss_metric,
            self.g_acc_metric,
        ]

    def train_step(self, real_images):
        # 잠재 공간에서 랜덤 포인트 샘플링
        batch_size = tf.shape(real_images)[0]
        random_latent_vectors = tf.random.normal(shape=(batch_size, self.latent_dim))

        # 가짜 이미지로 판별자 훈련
        with tf.GradientTape() as gen_tape, tf.GradientTape() as disc_tape:
            generated_images = self.generator(random_latent_vectors, training=True)
            real_predictions = self.discriminator(real_images, training=True)
            fake_predictions = self.discriminator(generated_images, training=True)

            real_labels = tf.ones_like(real_predictions)
            real_noisy_labels = real_labels + NOISE_PARAM * tf.random.uniform(tf.shape(real_predictions))
            fake_labels = tf.zeros_like(fake_predictions)
            fake_noisy_labels = fake_labels - NOISE_PARAM * tf.random.uniform(tf.shape(fake_predictions))

            d_real_loss = self.loss_fn(real_noisy_labels, real_predictions)
            d_fake_loss = self.loss_fn(fake_noisy_labels, fake_predictions)
            d_loss = (d_real_loss + d_fake_loss) / 2.0
            # d_loss = d_real_loss/2 + d_fake_loss/2

            g_loss = self.loss_fn(real_labels, fake_predictions)

        gradients_of_discriminator = disc_tape.gradient(d_loss, self.discriminator.trainable_variables)
        gradients_of_generator = gen_tape.gradient(g_loss, self.generator.trainable_variables)

        self.d_optimizer.apply_gradients(zip(gradients_of_discriminator, self.discriminator.trainable_variables))
        self.g_optimizer.apply_gradients(zip(gradients_of_generator, self.generator.trainable_variables))

        # 메트릭 업데이트
        self.d_loss_metric.update_state(d_loss)
        self.d_real_acc_metric.update_state(real_labels, real_predictions)
        self.d_fake_acc_metric.update_state(fake_labels, fake_predictions)
        self.d_acc_metric.update_state([real_labels, fake_labels], [real_predictions, fake_predictions])
        self.g_loss_metric.update_state(g_loss)
        self.g_acc_metric.update_state(real_labels, fake_predictions)

        return {m.name: m.result() for m in self.metrics}


def train_dcgan(dcgan):
    dcgan.compile(
        d_optimizer=optimizers.Adam(learning_rate=0.0002, beta_1=0.5, beta_2=0.999),
        g_optimizer=optimizers.Adam(learning_rate=0.0002, beta_1=0.5, beta_2=0.999),
    )

    checkpoint = callbacks.ModelCheckpoint(
        filepath="./models/dcgan-{epoch:02d}.weights.h5",
        save_weights_only=True,
    )

    # 학습이 오래 걸려 에포크 횟수를 300에서 100으로 축소
    dcgan.fit(train, epochs=100, callbacks=[checkpoint])
    dcgan.save_weight('./models/dcgan.weights.h5')


def show_visual(weight_path, train):
    dcgan.load_weights(weight_path)

    # 표준 정규 분포에서 잠재 공간의 일부 포인트 샘플링
    grid_width, grid_height = (10, 3)
    z_sample = np.random.normal(size=(grid_width * grid_height, Z_DIM))

    # 샘플링 포인트로 이미지 생성
    reconstructions = generator.predict(z_sample)

    fig = plt.figure(figsize=(18, 5))
    fig.subplots_adjust(hspace=0.4, wspace=0.4)

    # 그리드 형태로 출력
    for i in range(grid_width * grid_height):
        ax = fig.add_subplot(grid_height, grid_width, i + 1)
        ax.axis("off")
        ax.imshow(reconstructions[i, :, :], cmap="Greys")

    plt.show()

    # --------------------------------------------- #
    all_data = []
    for i in train.as_numpy_iterator():
        all_data.extend(i)
    all_data = np.array(all_data)

    r, c = 3, 5
    fig, axs = plt.subplots(r, c, figsize=(10, 6))
    fig.suptitle("Generated images", fontsize=20)

    noise = np.random.normal(size=(r * c, Z_DIM))
    gen_imgs = generator.predict(noise)

    cnt = 0
    for i in range(r):
        for j in range(c):
            axs[i, j].imshow(gen_imgs[cnt], cmap="gray_r")
            axs[i, j].axis("off")
            cnt += 1

    # plt.show()

    # --------------------------------------------- #
    def compare_images(img1, img2):
        return np.mean(np.abs(img1 - img2))

    # 생성 이미지에 대해 기존에 있는 모든 데이터로부터 가장 가까운 블록 검색
    fig, axs = plt.subplots(r, c, figsize=(10, 6))
    fig.suptitle("Closest images in the training set", fontsize=20)

    cnt = 0
    for i in range(r):
        for j in range(c):
            c_diff = 99999
            c_img = None
            for k_idx, k in enumerate(all_data):
                diff = compare_images(gen_imgs[cnt], k)
                if diff < c_diff:
                    c_img = np.copy(k)
                    c_diff = diff
            axs[i, j].imshow(c_img, cmap="gray_r")
            axs[i, j].axis("off")
            cnt += 1

    plt.show()


# DCGAN 생성
discriminator = make_discriminator()
generator = make_generator()
dcgan = DCGAN(discriminator, generator, latent_dim=Z_DIM)

train_data = utils.image_dataset_from_directory(
    "./lego_dataset/",
    labels=None,
    color_mode="grayscale",
    image_size=(IMAGE_SIZE, IMAGE_SIZE),
    batch_size=BATCH_SIZE,
    shuffle=True,
    seed=42,
    interpolation="bilinear",
)

train = train_data.map(lambda x: preprocess(x))
# train_sample = sample_batch(train)
# display(train_sample)

# 학습과 시각화 중에서 선택
# train_dcgan(dcgan)
show_visual('models/dcgan-100.weights.h5', train)

