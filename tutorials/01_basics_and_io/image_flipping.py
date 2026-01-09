import numpy as np
import cv2 as cv

image = cv.imread(r'..\..\image\ok.jpg',0)
rows,cols  = image.shape

matrix = np.float32([[1, 0,0],
                    [0,-1,rows],
                    [0,0,1]]) #Define the affine matrix for reflection (flip image horizontally)

reflected_image = cv.warpPerspective(image, matrix, (int(cols),int(rows)))

cv.imwrite(r'..\..\image\ok_reflected_image.jpg', reflected_image)