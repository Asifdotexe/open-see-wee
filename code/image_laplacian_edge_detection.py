import cv2 as cv

image = cv.imread(r'..\image\binary_one.png')
image_color = cv.imread(r'..\image\rickroll.jpg')

grayImage = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
grayImage_color = cv.cvtColor(image_color, cv.COLOR_BGR2GRAY)

laplacian = cv.Laplacian(grayImage, cv.CV_64F)
laplacian_color = cv.Laplacian(image_color, cv.CV_64F)
laplacian_color_grey = cv.Laplacian(grayImage_color, cv.CV_64F)

cv.imwrite(r'../image/hand_laplacian_edge_detection.jpg', laplacian)
cv.imwrite(r'../image/rick_laplacian_edge_detection.jpg', laplacian_color)
cv.imwrite(r'../image/rick_grey_laplacian_edge_detection.jpg', laplacian_color_grey)
