import cv2 as cv
import numpy as np

image = cv.imread('../image/luffy.jpg')
kernel = np.ones((15,15), np.uint8)

top_hat = cv.morphologyEx(image, cv.MORPH_BLACKHAT, kernel=kernel)
cv.imwrite('../image/luffy_black_hat_morphology.png', top_hat)