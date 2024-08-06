import cv2 as cv
# croping the image
image = cv.imread(r'..\image\ok.jpg')
cropped = image[500:900,500:900]