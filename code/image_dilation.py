import cv2 as cv
import numpy as np

image = cv.imread(r'..\image\binary_one.png')
image_rick = cv.imread(r'..\image\rickroll.jpg', cv.IMREAD_GRAYSCALE)

kernal= np.ones((3,3), np.uint8)
dilation_iter_1 = cv.dilate(image, kernal, iterations=1)
dilation_iter_2 = cv.dilate(image, kernal, iterations=2)
dilation_iter_3 = cv.dilate(image, kernal, iterations=3)
dilation_iter_4 = cv.dilate(image, kernal, iterations=4)
dilation_iter_5 = cv.dilate(image, kernal, iterations=5)

rick_dilation_iter_1 = cv.dilate(image_rick, kernal, iterations=1)
rick_dilation_iter_2 = cv.dilate(image_rick, kernal, iterations=2)
rick_dilation_iter_3 = cv.dilate(image_rick, kernal, iterations=3)
rick_dilation_iter_4 = cv.dilate(image_rick, kernal, iterations=4)
rick_dilation_iter_5 = cv.dilate(image_rick, kernal, iterations=5)

cv.imwrite(r'../image/hand_dilation_iter_1.jpg',dilation_iter_1)
cv.imwrite(r'../image/hand_dilation_iter_2.jpg',dilation_iter_2)
cv.imwrite(r'../image/hand_dilation_iter_3.jpg',dilation_iter_3)
cv.imwrite(r'../image/hand_dilation_iter_4.jpg',dilation_iter_4)
cv.imwrite(r'../image/hand_dilation_iter_5.jpg',dilation_iter_5)

cv.imwrite(r'../image/rick_dilation_iter_1.jpg',rick_dilation_iter_1)
cv.imwrite(r'../image/rick_dilation_iter_2.jpg',rick_dilation_iter_2)
cv.imwrite(r'../image/rick_dilation_iter_3.jpg',rick_dilation_iter_3)
cv.imwrite(r'../image/rick_dilation_iter_4.jpg',rick_dilation_iter_4)
cv.imwrite(r'../image/rick_dilation_iter_5.jpg',rick_dilation_iter_5)