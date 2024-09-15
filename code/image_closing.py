import cv2 as cv
import numpy as np

image = cv.imread(r'..\image\binary_one.png')
image_rick = cv.imread(r'..\image\rickroll.jpg', cv.IMREAD_GRAYSCALE)

kernal= np.ones((5,5), np.uint8)
close_hand = cv.morphologyEx(image, cv.MORPH_CLOSE ,kernal)
close_rick = cv.morphologyEx(image_rick, cv.MORPH_CLOSE ,kernal)

cv.imwrite(r'../image/hand_closing.jpg',close_hand)
cv.imwrite(r'../image/rick_closing.jpg',close_rick)