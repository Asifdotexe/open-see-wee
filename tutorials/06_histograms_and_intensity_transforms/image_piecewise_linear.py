import cv2 as cv
import numpy as np

image = cv.imread(r'..\..\image\ok.jpg')

row, col = image.shape[:2]
output_image = np.zeros((row, col), dtype='uint8')
range_min = 80
range_max = 140

for i in range(row):
    for j in range(col):
        if (image[i,j] > range_min).all() and (image[i,j] < range_max).all():
            output_image[i,j] = 255
        else:
            output_image[i,j] = image[i-1,j-1].min()
            
cv.imwrite(r'../../image/ok_piecewise_linear.jpg', output_image)