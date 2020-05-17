import tensorflow as tf
from tensorflow import keras

IMG_WIDTH = 64
IMG_HEIGHT = 64


def build_model():
    model = keras.models.Sequential()

    model.add(keras.layers.Conv2D(32, (3, 3), activation='relu',
                                  input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)))
    model.add(keras.layers.MaxPooling2D((2, 2)))
    model.add(keras.layers.Conv2D(32, (3, 3), activation='relu'))
    model.add(keras.layers.MaxPooling2D((2, 2)))
    model.add(keras.layers.Conv2D(32, (3, 3), activation='relu'))
    model.add(keras.layers.Dropout(0.2))

    model.add(keras.layers.Flatten())
    model.add(keras.layers.Dense(64, activation='relu'))
    model.add(keras.layers.Dense(17))

    model.compile(optimizer='adam', loss=tf.keras.losses.SparseCategoricalCrossentropy(
        from_logits=True), metrics=['accuracy'])

    return model
