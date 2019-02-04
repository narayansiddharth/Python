import numpy as np


class Activation:
    @staticmethod
    def activate(activation, layer_output):
        if activation == "":
            return 1
        return 0


class Layer:

    def __init__(self, layer_input, output_shape):
        self.layer_input = np.array(layer_input)
        self.layer_output = np.zeros(output_shape)
        self.weights = np.random.rand(self.layer_input.shape(), self.layer_output.shape()) - 0.5
        self.bias = np.random.rand(1, self.layer_output.shape()) - 0.5
        self.layer_loss = 0
        self.activation = ""
        self.activation_prime = ""

    def feed_forward(self):
        self.layer_output = Activation.activate(self.bias + np.dot(self.layer_input, self.weights))

    def update_loss(self, loss):
        self.layer_loss = loss

    def back_propagation(self):
        pass


class Network:
    pass
