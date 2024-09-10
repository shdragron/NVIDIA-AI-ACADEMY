import tensorflow as tf
import numpy as np

mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0
print(x_train.min(), x_train.max())
print(x_test.shape)
x_train = tf.expand_dims(x_train, axis=-1)
print(x_train.shape)
x_test = tf.expand_dims(x_test, axis=-1)
print(x_test.shape)

# list(dataset.as_numpy_iterator())

train_ds = tf.data.Dataset.from_tensor_slices((x_train, y_train)).shuffle(10000).batch(32)
test_ds = tf.data.Dataset.from_tensor_slices((x_test, y_test)).batch(32)

input = tf.keras.layers.Input(shape=(28, 28, 1))
x = tf.keras.layers.Conv2D(32, kernel_size=(3, 3), activation='relu')(input)
x = tf.keras.layers.MaxPooling2D(pool_size=(2, 2), padding = 'same')(x)
x = tf.keras.layers.Conv2D(64, kernel_size=(3, 3), activation='relu')(x)
x = tf.keras.layers.MaxPooling2D(pool_size=(2, 2), padding = 'same')(x)
x = tf.keras.layers.Flatten()(x)
x = tf.keras.layers.Dense(128, activation='relu')(x)
output = tf.keras.layers.Dense(10, activation='softmax')(x)

model = tf.keras.models.Model(inputs=input, outputs=output)

model.summary()

loss_function = tf.keras.losses.SparseCategoricalCrossentropy()
optimizer = tf.keras.optimizers.Adam(learning_rate=0.0001)

train_loss = tf.keras.metrics.Mean()
test_loss = tf.keras.metrics.Mean()
train_acc = tf.keras.metrics.SparseCategoricalAccuracy()
test_acc = tf.keras.metrics.SparseCategoricalAccuracy()

model.compile(loss=loss_function,optimizer=optimizer,metrics=['accuracy'])

def train_step(images, labels):
    with tf.GradientTape() as tape:
        predictions = model(images, training=True)
        loss = loss_function(labels, predictions)
        # print(loss)
    gradients = tape.gradient(loss, model.trainable_variables)
    optimizer.apply_gradients(zip(gradients, model.trainable_variables))
    train_loss(loss)
    train_acc(labels, predictions)

def test_step(images, labels):
    predictions = model(images, training=False)
    loss = loss_function(labels, predictions)

    test_loss(loss)
    test_acc(labels, predictions)


EPOCHS = 5

for epoch in range(EPOCHS):

    for images, labels in train_ds:
        # print(labels)
        train_step(images, labels)
    for test_images, test_labels in test_ds:
        test_step(test_images, test_labels)

    result = '에포크: {}, 손실: {:5f}, 정확도: {:2f}, test loss: {:5f}, test accuracy: {:2f}'
    print(result.format(epoch + 1,
                        train_loss.result(),
                        train_acc.result()*100,
                        test_loss.result(),
                        test_acc.result()*100))





