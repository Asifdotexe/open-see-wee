import cv2 as cv
import numpy as np

image = cv.imread('../image/luffy.jpg')
kernel = np.ones((15,15), np.uint8)

top_hat = cv.morphologyEx(image, cv.MORPH_TOPHAT, kernel=kernel)
cv.imwrite('../image/luffy_top_hat_morphology.png', top_hat)