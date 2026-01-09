import cv2 as cv
import numpy as np

image = cv.imread('../../image/ok.jpg')

kernel1 = np.array([[0,0,0],
                    [0,0,0],
                    [0,0,1]])

identify = cv.filter2D(src = image, ddepth = -1, kernel= kernel1)

cv.imwrite('../../image/ok_convolution_filter.jpg', identify)