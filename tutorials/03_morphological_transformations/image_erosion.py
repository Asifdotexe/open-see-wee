import cv2 as cv
import numpy as np

image = cv.imread(r'..\image\binary_one.png')
image_rick = cv.imread(r'..\image\rickroll.jpg', cv.IMREAD_GRAYSCALE)

kernal= np.ones((3,3), np.uint8)

erosion_iter_1 = cv.erode(image, kernal, iterations=1)
erosion_iter_2 = cv.erode(image, kernal, iterations=2)
erosion_iter_3 = cv.erode(image, kernal, iterations=3)
erosion_iter_4 = cv.erode(image, kernal, iterations=4)
erosion_iter_5 = cv.erode(image, kernal, iterations=5)

rick_erosion_iter_1 = cv.erode(image_rick, kernal, iterations=1)
rick_erosion_iter_2 = cv.erode(image_rick, kernal, iterations=2)
rick_erosion_iter_3 = cv.erode(image_rick, kernal, iterations=3)
rick_erosion_iter_4 = cv.erode(image_rick, kernal, iterations=4)
rick_erosion_iter_5 = cv.erode(image_rick, kernal, iterations=5)

cv.imwrite(r'../image/hand_erosion_iter_1.jpg',erosion_iter_1)
cv.imwrite(r'../image/hand_erosion_iter_2.jpg',erosion_iter_2)
cv.imwrite(r'../image/hand_erosion_iter_3.jpg',erosion_iter_3)
cv.imwrite(r'../image/hand_erosion_iter_4.jpg',erosion_iter_4)
cv.imwrite(r'../image/hand_erosion_iter_5.jpg',erosion_iter_5)

cv.imwrite(r'../image/rick_erosion_iter_1.jpg',rick_erosion_iter_1)
cv.imwrite(r'../image/rick_erosion_iter_2.jpg',rick_erosion_iter_2)
cv.imwrite(r'../image/rick_erosion_iter_3.jpg',rick_erosion_iter_3)
cv.imwrite(r'../image/rick_erosion_iter_4.jpg',rick_erosion_iter_4)
cv.imwrite(r'../image/rick_erosion_iter_5.jpg',rick_erosion_iter_5)