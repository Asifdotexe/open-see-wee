import cv2 as cv

image = cv.imread(r'..\image\binary_one.png')
image_color = cv.imread(r'..\image\rickroll.jpg')

median_blur_hand = cv.medianBlur(src=image, ksize=5)
gaussian_blur_hand = cv.GaussianBlur(src=image, ksize=(5,5), sigmaX=0, sigmaY=0,)

grayImage = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
grayImage_color = cv.cvtColor(image_color, cv.COLOR_BGR2GRAY)
grayImage_median_blur = cv.cvtColor(median_blur_hand, cv.COLOR_BGR2GRAY)
grayImage_gaussian_blur = cv.cvtColor(gaussian_blur_hand, cv.COLOR_BGR2GRAY)

sobely_gaussian = cv.Sobel(src=grayImage_gaussian_blur, ddepth=cv.CV_64F, dx=0, dy=1, ksize=5)
sobelx_gaussian = cv.Sobel(src=grayImage_gaussian_blur, ddepth=cv.CV_64F, dx=1, dy=0, ksize=5)
sobelxy_gaussian = cv.Sobel(src=grayImage_gaussian_blur, ddepth=cv.CV_64F, dx=1, dy=1, ksize=5)

sobely_median = cv.Sobel(src=grayImage_median_blur, ddepth=cv.CV_64F, dx=0, dy=1, ksize=5)
sobelx_median = cv.Sobel(src=grayImage_median_blur, ddepth=cv.CV_64F, dx=1, dy=0, ksize=5)
sobelxy_median = cv.Sobel(src=grayImage_median_blur, ddepth=cv.CV_64F, dx=1, dy=1, ksize=5)

cv.imwrite(r'../image/hand_gaussian_blur_and_sobel_x_edge_detection.jpg',sobelx_gaussian)
cv.imwrite(r'../image/hand_gaussian_blur_and_sobel_y_edge_detection.jpg',sobely_gaussian)
cv.imwrite(r'../image/hand_gaussian_blur_and_sobel_xy_edge_detection.jpg',sobelxy_gaussian)

cv.imwrite(r'../image/hand_median_blur_and_sobel_x_edge_detection.jpg',sobelx_median)
cv.imwrite(r'../image/hand_median_blur_and_sobel_y_edge_detection.jpg',sobely_median)
cv.imwrite(r'../image/hand_median_blur_and_sobel_xy_edge_detection.jpg',sobelxy_median)