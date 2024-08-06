import cv2 as cv

image = cv.imread(r'..\image\ok.jpg')
# creating a smaller mask image
resized_image = cv.resize(image, (256,256))
image_padded = cv.copyMakeBorder(resized_image,2,2,2,2,cv.BORDER_CONSTANT,None, value=(255,255,255))

cv.imwrite(r'..\image\neighbourhood_padded_image.jpg', image_padded)