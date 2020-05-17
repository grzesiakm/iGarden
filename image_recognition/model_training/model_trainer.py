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
    EPOCHS = 16

    generator = tf.keras.preprocessing.image.ImageDataGenerator(
        rescale=1./255)

    train_data_gen = generator.flow_from_directory(directory=str(data_dir) + "/train",
                                                   batch_size=BATCH_SIZE_TRAIN,
                                                   shuffle=True,
                                                   target_size=(
        width, height),
        classes=classes,
        class_mode="sparse")

    model = builder.build_model()
    model.fit(train_data_gen, epochs=EPOCHS)

    test_data_gen = generator.flow_from_directory(directory=str(data_dir) + "/test",
                                                  batch_size=BATCH_SIZE_TEST,
                                                  shuffle=True,
                                                  target_size=(
        width, height),
        classes=classes,
        class_mode="sparse")

    test_loss, test_acc = model.evaluate(test_data_gen)
    print("accuracy = ", test_acc)

    model.save("./saved/model.h5")
