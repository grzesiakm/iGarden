import numpy as np
import matplotlib.pyplot as plt

from tensorflow.keras.models import load_model

import image_load

test_images, test_labels = image_load.get_images_test()

encoder = load_model('saved/encoder')
decoder = load_model('saved/decoder')

encoder.compile()

encoded_imgs = encoder.predict(test_images)
decoded_imgs = decoder.predict(encoded_imgs)

X = []
Y = []

for img in encoded_imgs:
    X.append(img[0])
    Y.append(img[1])

for i in range(10):
    plt.scatter(X[i * 10: i * 10 + 10],
                Y[i * 10: i * 10 + 10], label=test_labels[i * 10])

plt.legend()
plt.show()

###Plot images###
# n = 10
# plt.figure(figsize=(16, 8))
# for i in range(n):
#     ax = plt.subplot(2, n, i + 1)
#     plt.imshow(test_images[i + 100].reshape(128, 128, 3))
#     ax.get_xaxis().set_visible(False)
#     ax.get_yaxis().set_visible(False)

#     ax = plt.subplot(2, n, i + 1 + n)
#     plt.imshow(decoded_imgs[i + 100].reshape(128, 128, 3))
#     ax.get_xaxis().set_visible(False)
#     ax.get_yaxis().set_visible(False)
# plt.show()
