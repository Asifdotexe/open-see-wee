import numpy as np
import cv2 as cv

image = cv.imread(r'..\image\ok.jpg',0)

rows,col  = image.shape
matrix = np.float32([[1,0,100],[0,1,100]]) # Affine matrix
translatedImage = cv.warpAffine(image,matrix,(col,rows))

cv.imwrite(r'..\image\ok_translatedImage.jpg', translatedImage)