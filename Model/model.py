MODEL_DIRECTORY = "model_v1_64.h5" 
#!!!!!!!!!!!! tu wpisujecie scieżke do modelu

import tensorflow as tf
from tensorflow import keras

import numpy as np
from PIL import Image


class Model:
    # wczytuje model z pliku
    def __init__(self):    
        self.model = tf.keras.models.load_model(MODEL_DIRECTORY)
        # names - wszystkie mozliwie kwiaty
        self.names = ["Daffodil", "Snowdrop", "LilyValley", "Bluebell", "Crocus", "Iris", "Tigerlily", "Tulip",
                      "Fritillary", "Sunflower", "Daisy", "ColtsFoot", "Dandelion", "Cowslip", "Buttercup", "Windflower", "Pansy"]
        self.IMG_SHAPE = 64

    # zwraca nazwe kwiatka
    # do wczytania pliku użyliśmy PIL
    def predict(self, image):   
        image = image.resize((self.IMG_SHAPE, self.IMG_SHAPE))
        image = np.array(image)
        image = np.expand_dims(image, axis=0)
        prediction = self.model.predict(image)
        return self.names[np.argmax(prediction[0])]
