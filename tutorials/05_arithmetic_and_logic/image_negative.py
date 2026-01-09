import cv2 as cv
import math

image = cv.imread('../../image/ok.jpg')
bw = cv.imread('../../image/binary_one.png')

#substract the value of each pixel from value value of intensity 
L = image.max()
M = bw.max()
image_negatives = L-image
bw_negatives = M - bw

cv.imwrite('../../image/image_negative.jpg', image_negatives)
cv.imwrite('../../image/bw_image_negative.jpg', bw_negatives)
