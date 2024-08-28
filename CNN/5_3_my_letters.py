# 5_3_my_letters.py

# 퀴즈:
# 우리가 만든 숫자 데이터에 대해 딥러닝 모델을 구축하세요. (제너레이터 사용)

import keras
from tensorflow.keras.preprocessing.image import ImageDataGenerator


gen_train = ImageDataGenerator(
                               rotation_range=0.25,)

flow_train = gen_train.flow_from_directory('letters/digit/train',
                               batch_size=1,
                               target_size=(39, 39),
                               class_mode='sparse',)

gen_test = ImageDataGenerator()

flow_test = gen_test.flow_from_directory('letters/digit/test',
                               batch_size=1,
                               target_size=(39, 39),
                               class_mode='sparse',)



model = keras.models.Sequential([

    keras.layers.Input(shape = [30,30,3]),
    # convolution Layer
    # 156 = 1 * 5*5 * 6 + 6
    keras.layers.Conv2D(6,5,1,'same',activation='relu',name='conv_1'),
    keras.layers.Conv2D(6,5,2,'same',activation='relu',name='conv_2'),
    # 2416 = 6 * 5*5 * 16 + 16
    keras.layers.Conv2D(16, 5, 1, 'valid', activation='relu', name='conv_3'),
    keras.layers.MaxPooling2D(2, name='pool_2'),

    # FC Layer
    # keras.layers.Flatten(),
    keras.layers.Flatten(name='flatten'),
    # 48120 = 400 * 120 + 120
    keras.layers.Dense(units=120, activation='relu',name='C_5'),
    # 10164 = 120 * 84 + 84
    keras.layers.Dense(units=84, activation='relu',name='F_6'),
    #  Output     Input      weight + bias
    # (? , 10) = (? , 84) @ (84, 10) + 10
    keras.layers.Dense(units=10, activation='softmax',name='Output'),
])

model.compile(optimizer=keras.optimizers.Adam(0.0001),
              loss=keras.losses.sparse_categorical_crossentropy,
              metrics=['acc'])

# model.fit(flow_train, epochs=10, verbose=1)

model.fit(flow_train, epochs=100, verbose=1,validation_data=flow_test)




