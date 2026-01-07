import numpy as np
import cv2 as cv

image = cv.imread(r'..\..\image\ok.jpg',0)
rows,cols  = image.shape

M = np.float32([[1,0.5,0],
                [0,1,0],
                [0,0,1]]) 
sheared_image = cv.warpPerspective(image, M, (int(cols*1.5),int(rows*1.5)))

cv.imwrite(r'..\..\image\ok_shearing_image.jpg', sheared_image)