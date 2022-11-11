import numpy as np

from data.image_loader import ImageLoader
from data.colors_representation import ColorsRepresentation
from model.cell import Cell,CellType
from view.colors import Color

class CurrentMapInitializer:
    def __init__(self, path_to_direct_img: str, path_to_velocity_img: str, image_loader: ImageLoader = ImageLoader()):
        self.direct_img = image_loader._get_image(path_to_direct_img, True)
        self.velocity_img = image_loader._get_image(path_to_velocity_img, False)
        if np.shape(self.direct_img)[:-1] != np.shape(self.velocity_img):
            raise Exception(f'Currents images have different sizes: {np.shape(self.direct_img)[:-1]},'
                            f'{np.shape(self.velocity_img)}')

    def get_image_size(self):
        return np.shape(self.velocity_img)

    def get_cell_arrays(self):
        (X, Y, Z) = np.shape(self.direct_img)
        array_d = np.empty(shape=(X, Y, 2), dtype=np.dtype(object))
        array_v = np.empty(shape=(X, Y), dtype=np.dtype(object))

        for x, row in enumerate(self.direct_img):
            for y, pixel in enumerate(row):
                if ColorsRepresentation.direction_dict.get(tuple(self.direct_img[x, y])) is None:
                    raise Exception(f'Image contains pixels in bad color: {tuple(self.direct_img[x, y])}, '
                                    f'Position: {x}, {y}')
                else:
                    array_d[x, y] = ColorsRepresentation.direction_dict.get(tuple(self.direct_img[x, y]))

        for x, row in enumerate(self.velocity_img):
            for y, pixel in enumerate(row):
                if ColorsRepresentation.current_vel_dict.get(self.velocity_img[x, y]) is None:
                    raise Exception(f'Image contains pixels in bad color: {self.velocity_img[x, y]}, '
                                    f'Position: {x}, {y}')
                else:
                    array_v[x, y] = ColorsRepresentation.current_vel_dict.get(self.velocity_img[x, y])
        return array_d, array_v
