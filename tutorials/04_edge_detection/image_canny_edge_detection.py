
import cv2 as cv

image = cv.imread(r'..\..\image\binary_one.png')
image_color = cv.imread(r'..\..\image\rickroll.jpg')

median_blur_hand = cv.medianBlur(src=image, ksize=5)
gaussian_blur_hand = cv.GaussianBlur(src=image, ksize=(7,7), sigmaX=0, sigmaY=0,)
gaussian_blur_rick = cv.GaussianBlur(src=image_color, ksize=(3,3), sigmaX=0, sigmaY=0,)

grayImage = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
grayImage_color = cv.cvtColor(image_color, cv.COLOR_BGR2GRAY)
grayImage_median_blur = cv.cvtColor(median_blur_hand, cv.COLOR_BGR2GRAY)
grayImage_gaussian_blur = cv.cvtColor(gaussian_blur_hand, cv.COLOR_BGR2GRAY)
rick_gaussian_blur = cv.cvtColor(gaussian_blur_rick, cv.COLOR_BGR2GRAY)

canny_gaussian = cv.Canny(grayImage_gaussian_blur, threshold1=100, threshold2=200)
canny_median = cv.Canny(grayImage_median_blur, threshold1=100, threshold2=200)
canny_gaussian_rick = cv.Canny(rick_gaussian_blur, threshold1=100, threshold2=120)

cv.imwrite(r'../../image/hand_canny_edge_detection.jpg',canny_gaussian)
cv.imwrite(r'../../image/rick_canny_edge_detection.jpg',canny_gaussian_rick)
cv.imwrite(r'../../image/hand_median_blur_and_canny_edge_detection.jpg',canny_median)
cv.imwrite(r'../../image/hand_gaussian_blur_and_canny_edge_detection.jpg',canny_gaussian)

