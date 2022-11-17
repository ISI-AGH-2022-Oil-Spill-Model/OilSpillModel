from data.image_loader import ImageLoader
import numpy as np


class WindSpeedScale:
    def __init__(self, vmin: float, vmax: float, image_loader: ImageLoader = ImageLoader()):
        self.scale = image_loader._get_image("images/scale.png", True)
        self.scale = np.squeeze(self.scale, 0)
        self.scale = np.unique(self.scale, axis=0)
        self.vmax = vmax
        self.vmin = vmin
        self.number_of_col = np.shape(self.scale)[0]

    def get_color2vel_dict(self):
        delta = (self.vmax - self.vmin) / (self.number_of_col - 1)
        color2vel_dict = {}
        for i in range(self.number_of_col):
            color2vel_dict[tuple(self.scale[i])] = self.vmin + i * delta
        return color2vel_dict
