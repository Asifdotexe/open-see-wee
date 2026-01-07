import cv2 as cv
import numpy as np

image = cv.imread(r'..\..\image\binary_one.png')
image_rick = cv.imread(r'..\..\image\rickroll.jpg', cv.IMREAD_GRAYSCALE)

kernal= np.ones((3,3), np.uint8)
open_hand = cv.morphologyEx(image, cv.MORPH_OPEN ,kernal)
open_rick = cv.morphologyEx(image_rick, cv.MORPH_OPEN ,kernal)

cv.imwrite(r'../../image/hand_opening.jpg',open_hand)
cv.imwrite(r'../../image/rick_opening.jpg',open_rick)