import cv2 as cv

image1 = cv.imread(r'..\..\image\binary_one.png')
image2 = cv.imread(r'..\..\image\binary_two.png')

height, width = image1.shape[:2]
image2_resized = cv.resize(image2, (width, height))

xor_image = cv.bitwise_xor(image1, image2_resized, mask=None)
cv.imwrite(r'../../image/bitwise_xor_binary.jpg', xor_image)