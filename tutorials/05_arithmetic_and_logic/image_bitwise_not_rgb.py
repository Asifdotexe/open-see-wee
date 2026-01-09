import cv2 as cv
import numpy as np

image = cv.imread('../../image/ok.jpg')

b, g, r = cv.split(image)

b_not = cv.bitwise_not(b)
g_not = cv.bitwise_not(g)
r_not = cv.bitwise_not(r)
not_image = cv.merge([b_not, g_not, r_not])
cv.imwrite('../../image/bitwise_not_rgb.jpg', not_image)
