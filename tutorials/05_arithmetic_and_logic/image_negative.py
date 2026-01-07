import cv2 as cv
import math

image = cv.imread(r'..\..\image\ok.jpg')
bw = cv.imread(r'..\..\image\binary_one.png')

#substract the value of each pixel from value value of intensity 
L = image.max()
M = bw.max()
image_negatives = L-image
bw_negatives = M - bw

cv.imwrite(r'../../image/image_negative.jpg', image_negatives)
cv.imwrite(r'../../image/bw_image_negative.jpg', bw_negatives)
