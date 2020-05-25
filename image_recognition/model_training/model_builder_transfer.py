import tensorflow as tf
from tensorflow import keras

IMG_WIDTH = 128
IMG_HEIGHT = 128


def build_model():
    model_base = tf.keras.applications.MobileNetV2(input_shape=(
        IMG_WIDTH, IMG_HEIGHT, 3), include_top=False, weights='imagenet')
    model_base.trainable = False

    model = keras.models.Sequential([model_base])

    model.add(keras.layers.GlobalAveragePooling2D())
    model.add(keras.layers.Dense(17))

    model.compile(optimizer='adam', loss=tf.keras.losses.SparseCategoricalCrossentropy(
        from_logits=True), metrics=['accuracy'])

    return model
