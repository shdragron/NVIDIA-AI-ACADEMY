from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, Flatten, Dense, Input
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping

import tensorflow as tf
import numpy as np
import os

mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0
print(x_train.shape, x_test.shape)
print(y_train.shape, y_test.shape)
print(len(x_train), len(x_test))

# 차원 1 증가
x_train = tf.expand_dims(x_train, axis=-1)
print(x_tran.shape)
x_test = tf.expand_dims(x_test, axis=-1)
print(x_test.shape)

class DataGenerator(tf.keras.utils.Sequence):
    def __init__(self, x_set, y_set, batch_size = 32):
        self.x = x_set
        self.y = y_set
        self.batch_size = batch_size

    def __len__(self):
        return int(np.floor(len(self.x) / self.batch_size))

    def __getitem__(self, index):
        print('indx: ', index)
        batch_x = self.x[index * self.batch_size:(index + 1) * self.batch_size]
        batch_y = self.y[index * self.batch_size:(index + 1) * self.batch_size]
        return batch_x, batch_y

generator_train = DataGenerator(x_train, y_train, batch_size=32)
generator_test = DataGenerator(x_test, y_test, batch_size=32)


input = Input(shape=(28, 28, 1))
x = Conv2D(32, (3, 3), activation='relu')(input)
x = Conv2D(64, (3, 3), activation='relu')(x)
x = Flatten()(x)
x = Dense(128, activation='relu')(x)
x = Dense(10, activation='softmax')(x)

model = tf.keras.models.Model(inputs=input, outputs=x)
model.summary()
model.compile(loss= tf.keras.losses.SparseCategoricalCrossentropy(), optimizer='adam', metrics=['accuracy','val_loss'])



save_dir = 'C:/Users/Harmony05/Desktop/NVIDIA-AI-ACADEMY/NVIDIA-AI-ACADEMY/Object_detection/2.YoloV1/Squence_generator/model'
weights_path = os.path.join(save_dir, 'yolov1_weights.hdf5')
checkpoint = ModelCheckpoint(weights_path, monitor='loss',
                                 save_weights_only=True, save_best_only=True)

early_stopping = EarlyStopping(
        monitor='loss', patience=3, verbose=1)



if os.path.exists(weights_path):
    # by_name = True ==> 같은 이름의 layer에 가중치 로딩
    model.load_weights(weights_path, by_name=True)
    print('complete loading yolov1_weights ')
else:
    print('no train history')


# model.fit(generator, epochs=2, shuffle=False, callbacks=[checkpoint, early_stopping])

weights_path_1 = './model/yolov1_weights.hdf5'
model.load_weights(weights_path_1)

# 모델 예측
preds = model.predict(x_test[:5])
# print(preds[:5])
print(y_test[:5])
print(np.argmax(preds[:5],axis=1))
