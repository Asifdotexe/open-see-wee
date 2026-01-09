import cv2 as cv
import numpy as np

image1 = cv.imread('../../image/shinchan.png')
image2 = cv.imread('../../image/ok.jpg')

height, width = image1.shape[:2]
image2_resized = cv.resize(image2, (width, height))

b1, g1, r1 = cv.split(image1)
b2, g2, r2 = cv.split(image2_resized)

b_xor = cv.bitwise_xor(b1, b2)
g_xor = cv.bitwise_xor(g1, g2)
r_xor = cv.bitwise_xor(r1, r2)
xor_image = cv.merge([b_xor, g_xor, r_xor])
cv.imwrite('../../image/bitwise_xor_rgb.jpg', xor_image)
