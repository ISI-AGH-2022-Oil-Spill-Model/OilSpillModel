import cv2
import numpy as np
import os


class ImageLoader:

    def _get_image(self, path_to_image: str, isColorful: bool):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        path_to_image = os.path.abspath(os.path.join(dir_path, os.pardir)) + path_to_image
        if isColorful:
            img = cv2.imread(path_to_image)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img = np.transpose(img, (1, 0, 2))
        else:
            img = cv2.imread(path_to_image,cv2.IMREAD_GRAYSCALE)
            img = np.transpose(img, (1, 0))
        return img