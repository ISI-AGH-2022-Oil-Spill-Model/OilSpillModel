import numpy as np

from applicators.i_applicator import IApplicator
from model.change_matrix import ChangeMatrix
from model.model import Model


def dispersion(x, y, x2, y2, oil_level, modified, modifier):
    change = oil_level[x2, y2] * modifier

    # condition which prevents from creating negative values in cells in case of
    # too big dispersion constants or oil layer being too thin

    if oil_level[x2, y2] - 4 * change > 0:
        modified[x, y] += change
        modified[x2, y2] -= change
    return modified




class DispersionApplicator(IApplicator):

    def __init__(self, diagonal_dispersion_modifier, dispersion_constant):
        self.D = diagonal_dispersion_modifier
        self.P = dispersion_constant

    def apply(self, model: Model, change_matrix: ChangeMatrix) -> ChangeMatrix:
        oil_level = model.oil_level
        x_max = oil_level.shape[0]
        y_max = oil_level.shape[1]

        self.disperse_outwards(1, 0, oil_level, oil_level)

        changes = np.zeros(oil_level.shape)
        for x in range(x_max):
            for y in range(y_max):

                self.disperse_outwards(x, y, oil_level, changes)

        change_matrix.oil_level = changes
        return change_matrix

    def disperse_outwards(self, x, y, oil_level, modified_oil_level) -> np.array:
        oil = oil_level[x, y]
        max_x = oil_level.shape[0] - 1
        max_y = oil_level.shape[1] - 1

        neighbours = np.empty(shape=(0, 2), dtype=np.int16)
        if x > 0 and oil_level[x - 1, y] < oil:
            neighbours = np.append(neighbours, [[x - 1, y]], axis=0)
        if y < max_y and oil_level[x, y + 1] < oil:
            neighbours = np.append(neighbours, [[x, y + 1]], axis=0)
        if x < max_x and oil_level[x + 1, y] < oil:
            neighbours = np.append(neighbours, [[x + 1, y]], axis=0)
        if y > 0 and oil_level[x, y - 1] < oil:
            neighbours = np.append(neighbours, [[x, y - 1]], axis=0)

        diagonals = np.empty(shape=(0, 2), dtype=np.int16)
        if x > 0 and y > 0 and oil_level[x - 1, y - 1] < oil:
            diagonals = np.append(diagonals, [[x - 1, y - 1]], axis=0)
        if x > 0 and y < max_y and oil_level[x - 1, y + 1] < oil:
            diagonals = np.append(diagonals, [[x - 1, y + 1]], axis=0)
        if x < max_x and y < max_y and oil_level[x + 1, y + 1] < oil:
            diagonals = np.append(diagonals, [[x + 1, y + 1]], axis=0)
        if x < max_x and y > 0 and oil_level[x + 1, y - 1] < oil:
            diagonals = np.append(diagonals, [[x + 1, y - 1]], axis=0)

        n_amount = len(neighbours)
        n_change = oil_level[x, y] * self.P
        d_amount = len(diagonals)
        d_change = oil_level[x, y] * self.D

        while n_change * n_amount + d_change * d_amount > oil_level[x, y]:
            if n_amount != 0:
                n_change /= n_amount
            if d_amount != 0:
                d_change /= d_amount

        modified_oil_level[x, y] -= (n_change + d_change)

        for n in neighbours:
            modified_oil_level[n[0], n[1]] += n_change / n_amount

        for d in diagonals:
            modified_oil_level[d[0], d[1]] += d_change / d_amount

