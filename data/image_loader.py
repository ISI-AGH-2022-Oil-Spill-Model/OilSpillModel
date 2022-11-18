import cv2
import numpy as np
import os


class ImageLoader:

    def _get_image(self, path_to_image: str, is_colorful: bool):
        if is_colorful:
            img = cv2.imread(path_to_image)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        else:
            img = cv2.imread(path_to_image,cv2.IMREAD_GRAYSCALE)
        print(img.shape)
        return img