import cv2 as cv
import numpy as np

image = cv.imread(r'..\..\image\ok.jpg')

kernel1 = np.array([[0,0,0],
                    [0,0,0],
                    [0,0,1]])

identify = cv.filter2D(src = image, ddepth = -1, kernel= kernel1)

cv.imwrite(r'..\..\image\ok_convolution_filter.jpg', identify)