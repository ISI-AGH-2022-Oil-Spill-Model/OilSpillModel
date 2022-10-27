import cv2
import os


class ImageLoader:

    def _get_image(self, path_to_image: str):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        path_to_image = os.path.abspath(os.path.join(dir_path, os.pardir)) + path_to_image
        img = cv2.imread(path_to_image)
        return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)