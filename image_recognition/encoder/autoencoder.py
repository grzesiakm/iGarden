import tensorflow as tf
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.models import Model
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import pathlib
from os import listdir
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

images = listdir('images/')
image_array = []
for image in images:
    image = Image.open('images/' + image)
    image = image.resize((128, 128))
    image = np.array(image)/255
    image_array.append(image)
image_array = np.asarray(image_array)
images_train = image_array[0: int(len(images)*.7)]
images_test = image_array[int(len(images)*.7): -1]

images_train = images_train.reshape(
    len(images_train), np.prod(images_train.shape[1:]))
images_test = images_test.reshape(
    len(images_test), np.prod(images_test.shape[1:]))

input_dims = (128, 128, 3)
input_img = Input(shape=(np.prod(input_dims),))

encoding_dim = 1024

encoded = Dense(encoding_dim, activation='relu')(input_img)
decoded = Dense(128*128*3, activation='sigmoid')(encoded)

autoencoder = Model(input_img, decoded)
encoder = Model(input_img, encoded)

encoded_input = Input(shape=(encoding_dim,))
decoder_layer = autoencoder.layers[-1]
decoder = Model(encoded_input, decoder_layer(encoded_input))

autoencoder.compile(optimizer='adam', loss='binary_crossentropy')

autoencoder.fit(images_train, images_train, epochs=15, batch_size=32,
                shuffle=True, validation_data=(images_test, images_test))


encoded_imgs = encoder.predict(images_test)
decoded_imgs = decoder.predict(encoded_imgs)


n = 10
plt.figure(figsize=(16, 8))
for i in range(n):
    ax = plt.subplot(2, n, i + 1)
    plt.imshow(images_test[i].reshape(128, 128, 3))
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    ax = plt.subplot(2, n, i + 1 + n)
    plt.imshow(decoded_imgs[i].reshape(128, 128, 3))
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
plt.show()
