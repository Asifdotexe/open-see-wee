import cv2 as cv

image = cv.imread(r'..\..\image\ok.jpg')
cropped = image[500:900,500:900]

cv.imwrite(r'..\..\image\cropped_ok.jpg', cropped)