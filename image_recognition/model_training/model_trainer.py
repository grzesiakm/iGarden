import tensorflow as tf
from tensorflow import keras

import numpy as np
import pathlib

import model_builder as builder


def train_model():
    data_dir = ("flowers_sorted")
    data_dir = pathlib.Path(data_dir)

    width = builder.IMG_WIDTH
    height = builder.IMG_HEIGHT
    classes = ["Daffodil", "Snowdrop", "LilyValley", "Bluebell", "Crocus", "Iris", "Tigerlily", "Tulip",
               "Fritillary", "Sunflower", "Daisy", "ColtsFoot", "Dandelion", "Cowslip", "Buttercup", "Windflower", "Pansy"]

    BATCH_SIZE_TRAIN = 32
    BATCH_SIZE_TEST = 32
    EPOCHS = 64

    generator = tf.keras.preprocessing.image.ImageDataGenerator(
        rescale=1./255)

    generator_modified = keras.preprocessing.image.ImageDataGenerator(rescale=1./255.,
                                                                      rotation_range=45,
                                                                      width_shift_range=.15,
                                                                      height_shift_range=.15,
                                                                      horizontal_flip=True,
                                                                      zoom_range=0.5
                                                                      )

    train_data_gen = generator_modified.flow_from_directory(directory=str(data_dir) + "/train",
                                                            batch_size=BATCH_SIZE_TRAIN,
                                                            shuffle=True,
                                                            target_size=(
        width, height),
        classes=classes,
        class_mode="sparse")
    val_data_gen = generator.flow_from_directory(directory=str(data_dir) + "/test",
                                                 batch_size=BATCH_SIZE_TEST,
                                                 shuffle=True,
                                                 target_size=(
        width, height),
        classes=classes,
        class_mode="sparse")

    model = builder.build_model()
    history = model.fit(train_data_gen, epochs=EPOCHS,
                        validation_data=val_data_gen)

    model.save("model.h5")

    return history


if __name__ == "__main__":
    train_model()
