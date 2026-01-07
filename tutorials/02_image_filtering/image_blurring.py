#Sharp to blur image
import cv2 as cv
import numpy as np

image = cv.imread(r'..\..\image\ok.jpg')

kernel2 = np.ones((5,5),np.float64(32))/25

blurImage = cv.filter2D(src=image, ddepth=-1, kernel = kernel2)

cv.imwrite(r'..\..\image\ok_image_blurred.png', blurImage)