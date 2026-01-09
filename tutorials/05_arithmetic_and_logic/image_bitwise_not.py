import cv2 as cv

image1 = cv.imread('../../image/binary_one.png')
image2 = cv.imread('../../image/binary_two.png')

height, width = image1.shape[:2]
image2_resized = cv.resize(image2, (width, height))

not_image1 = cv.bitwise_not(image1, mask=None)
not_image2 = cv.bitwise_not(image2_resized, mask=None)
cv.imwrite('../../image/bitwise_not_binary_one.jpg', not_image1)
cv.imwrite('../../image/bitwise_not_binary_two.jpg', not_image2)
