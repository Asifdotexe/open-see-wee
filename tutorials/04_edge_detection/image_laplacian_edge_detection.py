import cv2 as cv

image = cv.imread(r'..\image\binary_one.png')
image_color = cv.imread(r'..\image\rickroll.jpg')

median_blur_hand = cv.medianBlur(src=image, ksize=5)
gaussian_blur_hand = cv.GaussianBlur(src=image, ksize=(3,3), sigmaX=0, sigmaY=0,)

grayImage = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
grayImage_color = cv.cvtColor(image_color, cv.COLOR_BGR2GRAY)
grayImage_median_blur = cv.cvtColor(median_blur_hand, cv.COLOR_BGR2GRAY)
grayImage_gaussian_blur = cv.cvtColor(gaussian_blur_hand, cv.COLOR_BGR2GRAY)

laplacian = cv.Laplacian(grayImage, cv.CV_64F)
laplacian_color = cv.Laplacian(image_color, cv.CV_64F)
laplacian_color_grey = cv.Laplacian(grayImage_color, cv.CV_64F)
laplacian_hand_median_blur = cv.Laplacian(grayImage_median_blur, cv.CV_64F)
laplacian_hand_gaussian_blur = cv.Laplacian(grayImage_gaussian_blur, cv.CV_64F)

cv.imwrite(r'../image/hand_laplacian_edge_detection.jpg', laplacian)
cv.imwrite(r'../image/rick_laplacian_edge_detection.jpg', laplacian_color)
cv.imwrite(r'../image/rick_grey_laplacian_edge_detection.jpg', laplacian_color_grey)
cv.imwrite(r'../image/hand_median_blur_and_laplacian_edge_detection.jpg', laplacian_hand_median_blur)
cv.imwrite(r'../image/hand_gaussian_blur_and_laplacian_edge_detection.jpg', laplacian_hand_gaussian_blur)