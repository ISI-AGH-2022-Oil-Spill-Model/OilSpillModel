import cv2
import numpy as np
import os


class ImageLoader:

    def _get_image(self, path_to_image: str, is_colorful: bool):
        if is_colorful:
            img = cv2.imread(path_to_image)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img = np.transpose(img, (1, 0, 2))
        else:
            img = cv2.imread(path_to_image,cv2.IMREAD_GRAYSCALE)
            img = np.transpose(img, (1, 0))
        return img