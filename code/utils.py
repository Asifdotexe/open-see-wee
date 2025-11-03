import numpy as np
import cv2 as cv

def resize_to_match(img_1: np.ndarray, img_2: np.ndarray) -> np.ndarray:
    """
    Resizes both the image to be the exact dimensions (height, width)

    :param img_1: The reference image whose dimensions will be copied.
    :param img_2: The image that will be resized.
    :return: A new image (a resized version of img_2) with the same height and width as img_1.
    """
    height, width = img_1.shape[:2]
    return cv.resize(img_2, (width, height))
