import cv2 as cv

# RBG
image = cv.imread(r'..\image\ok.jpg')
# print(image.shape)

# upsampling
imageUpSampled = cv.pyrUp(image)
cv.imwrite(r'..\image\ok_upsampled.jpg', imageUpSampled)

# downsampling
imageDownSample = cv.pyrDown(image)
cv.imwrite(r'..\image\ok_downsampled.jpg', imageDownSample)

