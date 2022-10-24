import numpy as np

from model.change_matrix import ChangeMatrix


class Model:

    def __init__(self, shape: tuple):
        self.shape = shape
        self.oil_level = np.zeros(shape)

    def apply_change(self, change_matrix: ChangeMatrix):
        pass
