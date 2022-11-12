import numpy as np

from data.image_loader import ImageLoader
from data.wind_speed_scale import WindSpeedScale
from data.colors_representation import ColorsRepresentation

class WindMapInitializer:
    def __init__(self, path_to_vel: str, path_to_dir: str,image_loader: ImageLoader = ImageLoader(),
                 scale: WindSpeedScale = WindSpeedScale()):
        self.vel = image_loader._get_image(path_to_vel, True)
        self.dir = image_loader._get_image(path_to_dir, True)
        self.color2vel = scale.get_color2vel_dict()
    def get_arrays(self):
        (X, Y, Z) = np.shape(self.vel)
        array_v = np.empty(shape=(X, Y), dtype=np.dtype(object))
        array_d = np.empty(shape=(X, Y, 2), dtype=np.dtype(object))
        for x, row in enumerate(self.vel):
            for y, pixel in enumerate(row):
                if np.array_equal(pixel, np.array([0,0,0])):
                    array_v[x,y]=0
                elif self.color2vel.get(tuple(self.vel[x, y])) is None:
                    raise Exception(f'Image contains pixels in bad color: {tuple(self.vel[x, y])}, '
                                    f'Position: {x}, {y}')
                else:
                    array_v[x, y] = self.color2vel.get(tuple(self.vel[x, y]))
        for x, row in enumerate(self.dir):
            for y, pixel in enumerate(row):
                if ColorsRepresentation.direction_dict.get(tuple(self.dir[x, y])) is None:
                    raise Exception(f'Image contains pixels in bad color: {tuple(self.dir[x, y])}, '
                                    f'Position: {x}, {y}')
                else:
                    array_d[x, y] = ColorsRepresentation.direction_dict.get(tuple(self.dir[x, y]))
        return array_v, array_d
