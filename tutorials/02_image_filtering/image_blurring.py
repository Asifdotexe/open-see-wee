#Sharp to blur image
import cv2 as cv
import numpy as np

image = cv.imread('../../image/ok.jpg')

kernel2 = np.ones((5,5),np.float64(32))/25

blurImage = cv.filter2D(src=image, ddepth=-1, kernel = kernel2)

cv.imwrite('../../image/ok_image_blurred.png', blurImage)