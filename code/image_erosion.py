import cv2 as cv
import numpy as np

image = cv.imread(r'..\image\binary_one.png')

kernal= np.ones((5,5), np.uint8)
erosion_iter_1 = cv.erode(image, kernal, iterations=1)
erosion_iter_2 = cv.erode(image, kernal, iterations=2)
erosion_iter_3 = cv.erode(image, kernal, iterations=3)
erosion_iter_4 = cv.erode(image, kernal, iterations=4)
erosion_iter_5 = cv.erode(image, kernal, iterations=5)

cv.imwrite(r'../image/hand_erosion_iter_1.jpg',erosion_iter_1)
cv.imwrite(r'../image/hand_erosion_iter_2.jpg',erosion_iter_2)
cv.imwrite(r'../image/hand_erosion_iter_3.jpg',erosion_iter_3)
cv.imwrite(r'../image/hand_erosion_iter_4.jpg',erosion_iter_4)
cv.imwrite(r'../image/hand_erosion_iter_5.jpg',erosion_iter_5)
