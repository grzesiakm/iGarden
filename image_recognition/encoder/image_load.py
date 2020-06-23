from os import listdir
import pathlib
from PIL import Image
import numpy as np


def get_images_train():
    images = listdir('images/')
    image_array = []

    for image in images:
        image = Image.open('images/' + image)
        image = image.resize((128, 128))
        image = np.array(image)/255
        image_array.append(image)

    image_array = np.asarray(image_array)

    images_train = image_array.reshape(
        len(image_array), np.prod(image_array.shape[1:]))

    return images_train


def get_images_test():
    labels = listdir('test/')
    test_images = []
    test_labels = []
    for label in labels:
        images = listdir('test/' + label + '/')
        for image in images:
            image = Image.open('test/' + label + '/' + image)
            image = image.resize((128, 128))
            image = np.array(image)/255
            test_images.append(image)
            test_labels.append(label)

    test_images = np.asarray(test_images)
    test_images = test_images.reshape(
        len(test_images), np.prod(test_images.shape[1:]))

    return test_images, test_labels
