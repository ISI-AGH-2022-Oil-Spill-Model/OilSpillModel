import numpy as np


class ChangeMatrix:

    def __init__(self, shape):
        self.oil_level = np.zeros(shape)
        self.shape = shape

    def clear(self):
        self.oil_level.fill(0)
