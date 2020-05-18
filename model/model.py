from PIL import Image
import numpy as np
from tensorflow import keras
import tensorflow as tf
import os
from django.conf import settings
MODEL_DIRECTORY = os.path.join(settings.BASE_DIR, 'model/model_18_05_20.h5')


class Model:
    def __init__(self):
        self.model = tf.keras.models.load_model(MODEL_DIRECTORY)
        self.names = ["Daffodil", "Snowdrop", "LilyValley", "Bluebell", "Crocus", "Iris", "Tigerlily", "Tulip",
                      "Fritillary", "Sunflower", "Daisy", "ColtsFoot", "Dandelion", "Cowslip", "Buttercup", "Windflower", "Pansy"]
        self.IMG_SHAPE = 64

    def predict(self, image):
        image = image.resize((self.IMG_SHAPE, self.IMG_SHAPE))
        image = np.array(image)
        image = np.expand_dims(image, axis=0)
        prediction = self.model.predict(image)
        found_index = np.argmax(prediction[0])
        return (self.names[found_index], found_index)
