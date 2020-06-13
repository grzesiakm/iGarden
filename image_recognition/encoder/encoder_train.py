import tensorflow as tf
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.models import Model
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import numpy as np


import image_load

train_images = image_load.get_images_train()
test_images, test_labels = image_load.get_images_test()


input_dims = (128, 128, 3)
input_img = Input(shape=(np.prod(input_dims),))

encoding_dim = [1024, 128, 2]

encoded = Dense(encoding_dim[0], activation='relu')(input_img)
encoded = Dense(encoding_dim[1], activation='relu')(encoded)
encoded = Dense(encoding_dim[2], activation='relu')(encoded)

decoded = Dense(128, activation='relu')(encoded)
decoded = Dense(1024, activation='relu')(decoded)
decoded = Dense(128*128*3, activation='sigmoid')(decoded)


autoencoder = Model(input_img, decoded)
encoder = Model(input_img, encoded)

encoded_input = Input(shape=(encoding_dim[-1],))
decoder_layers = autoencoder.layers[-3](encoded_input)
decoder_layers = autoencoder.layers[-2](decoder_layers)
decoder_layers = autoencoder.layers[-1](decoder_layers)

decoder = Model(encoded_input, decoder_layers)

autoencoder.compile(optimizer='adam', loss='binary_crossentropy')

autoencoder.fit(train_images, train_images, epochs=20, batch_size=32,
                shuffle=True, validation_data=(test_images, test_images))

decoder.save('saved/decoder')
encoder.save('saved/encoder')
