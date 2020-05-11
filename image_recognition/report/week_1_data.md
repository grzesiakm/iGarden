DATA:
We used data set from: https://www.robots.ox.ac.uk/~vgg/data/flowers/17/index.html. There are 17 types of flower with 80 images for each.
We split the data into 2 groups: train and test in a 70:10 ratio for each flower. During the training we spot a problem with low amount of unique flowers. It makes the neural network more prone to overfitting and the predictions are not very accurate.
We are planning to modify images in random way: scaling, rotating, cutting part of the image. It will artificially increase amount of training images.