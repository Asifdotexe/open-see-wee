import cv2 as cv
import numpy as np

image = cv.imread('../../image/luffy.jpg')
kernel = np.ones((3,3), np.uint8)

morph_gradient = cv.morphologyEx(image, cv.MORPH_GRADIENT, kernel)
cv.imwrite('../../image/morph_gradient_luffy.png', morph_gradient)