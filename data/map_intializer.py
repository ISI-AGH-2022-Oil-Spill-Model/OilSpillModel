import numpy as np

from data.image_loader import ImageLoader
from model.cell import Cell,CellType
from view.colors import Color

class MapInitializer:
    def __init__(self, path_to_img: str, image_loader: ImageLoader = ImageLoader()):
        self.image = image_loader._get_image(path_to_img, True)

    def get_image_size(self):
        return np.shape(self.image)[:2]

    def get_cell_array(self, cell_size: int):
        (X, Y, Z) = np.shape(self.image)
        array = np.empty(shape=(X, Y), dtype=np.dtype(object))
        for x, row in enumerate(self.image):
            for y, pixel in enumerate(row):
                c_type = 0
                pixel_list = tuple(pixel)
                match pixel_list:
                    case Color.water:
                        c_type = CellType.WATER
                    case Color.earth:
                        c_type = CellType.EARTH
                    case Color.oil:
                        c_type = CellType.OIL_SOURCE
                    case _:
                        raise Exception("Image contains pixels in bad color!")
                array[x, y] = Cell(c_type, cell_size, x, y)
        return array
