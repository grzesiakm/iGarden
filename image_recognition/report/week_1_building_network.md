Machine learning framework used for the project: tensorflow with keras.

For the first version of the network we decided to build a simple Convolutional Neural Network.

The network consist of a stack of layers defined in keras framework: Conv2D which are kernels being trained and MaxPooling2D used to downsample input.

Final layers of the network are Flatten which transform data into one dimension and Dense that makes actual classification.

Steps for creating CNN using keras library:
 - Creating model using keras.models.Sequential().
 - Adding layers to model with model.add().
 - Compiling the model with model.compile().
 - Training the model using model.fit().