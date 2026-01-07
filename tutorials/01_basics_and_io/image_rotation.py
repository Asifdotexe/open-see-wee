import cv2 as cv
import numpy as np

image = cv.imread(r'..\..\image\ok.jpg',0)
rows,cols  = image.shape

M = np.float32([[1,0,0],
                [0,-1,rows],
                [0,0,1]]) # Define the affine matrix for rotation

rotated_image = cv.warpAffine(image, cv.getRotationMatrix2D((cols/2,rows/2),90,0.6), (cols,rows))
cv.imwrite(r'..\..\image\ok_rotated_image.jpg', rotated_image)
x