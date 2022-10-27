import numpy as np

from data.image_loader import ImageLoader
from model.cell import Cell,CellType

class MapInitializer:
    def __init__(self, path_to_img: str):
        self.image = ImageLoader._get_image(path_to_img)

    def getCellArray(self, cell_size: int):
        (X, Y) = np.shape(self.image)
        array=np.zeros(shape=(X, Y))
        for x in range(X):
            for y in range(Y):
                (r, g, b) = self.image[x, y]
                c_type = 0
                if b == 0:
                    c_type = CellType.WATER
                elif g == 0:
                    c_type = CellType.EARTH
                elif r == g == b == 0:
                    c_type = CellType.OIL_SOURCE
                else:
                    raise ("Image contains pixels in bad color!")
                array[x, y] = Cell(type=c_type, cell_size=cell_size, row=x, col=y)
        return array
