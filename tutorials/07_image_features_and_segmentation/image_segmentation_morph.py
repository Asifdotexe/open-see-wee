import cv2 as cv
import numpy as np
image = cv.imread("../../image/coins_image.jpg")
if image is None:
    raise RuntimeError("Failed to load image from ../../image/coins_image.jpg")
image_gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
ret , thresh = cv.threshold(image_gray,103.555,255,cv.THRESH_BINARY + cv.THRESH_OTSU)
cv.imshow("Threshold Image",thresh)
cv.waitKey(0)

kernel = np.ones((3,3),np.uint8)
opening = cv.morphologyEx(thresh,cv.MORPH_OPEN,kernel,iterations=2)

#extract background region 
bg = cv.dilate(opening,kernel,iterations=3)

#display background region
#extract foreground region
distransform = cv.distanceTransform(opening,cv.DIST_L2,5)
ret,fg = cv.threshold(distransform,0.7*distransform.max(),255,0)
#display the segmented foreground region 

cv.imshow("Background",bg)
cv.waitKey(0)
cv.destroyAllWindows()

cv.imshow("Foreground",fg)
cv.waitKey(0)
cv.destroyAllWindows()