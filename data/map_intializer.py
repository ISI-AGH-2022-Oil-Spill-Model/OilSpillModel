import numpy as np

from data.image_loader import ImageLoader
from model.cell import Cell,CellType
from view.colors import Color

class MapInitializer:
    def __init__(self, path_to_img: str, image_loader: ImageLoader = ImageLoader()):
        self.image = image_loader._get_image(path_to_img)

    def get_image_size(self):
        return np.shape(self.image)[:2]

    def get_cell_array(self, cell_size: int):
        (X, Y, Z) = np.shape(self.image)
        array = np.empty(shape=(X, Y), dtype=np.dtype(object))
        for y in range(Y):
            for x in range(X):
                pixel_rgb = self.image[y,x]
                c_type = 0
                if np.array_equal(pixel_rgb, np.array(Color.water)):
                    c_type = CellType.WATER
                elif np.array_equal(pixel_rgb, np.array(Color.earth)):
                    c_type = CellType.EARTH
                elif np.array_equal(pixel_rgb, np.array(Color.oil)):
                    c_type = CellType.OIL_SOURCE
                else:
                    raise ("Image contains pixels in bad color!")
                array[x, y] = Cell(c_type, cell_size, x, y)
        return array
