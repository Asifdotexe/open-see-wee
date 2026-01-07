import cv2 as cv
import numpy as np

image = cv.imread(r'..\..\image\ok.jpg')
shinchan = cv.imread(r'..\..\image\shinchan.png')

emboss_kernal = np.array([
    [-1,0,0],
    [0,0,0],
    [0,0,1]
])

emboss_image = cv.filter2D(src=image, ddepth=-1, kernel=emboss_kernal)
emboss_shinchan = cv.filter2D(src=shinchan, ddepth=-1, kernel=emboss_kernal)

cv.imwrite(r'..\..\image\ok_emboss.png', emboss_image)
cv.imwrite(r'..\..\image\shinchan_emboss.png', emboss_shinchan)
