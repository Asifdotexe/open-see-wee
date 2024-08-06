import cv2 as cv
import numpy as np

image = cv.imread(r'..\image\ok.jpg')

b, g, r = cv.split(image)

b_not = cv.bitwise_not(b)
b_not = cv.bitwise_not(g)
b_not = cv.bitwise_not(r)
not_image = cv.merge([b_not, b_not, b_not])
cv.imwrite(r'..\image\bitwise_not_rgb.jpg', not_image)
