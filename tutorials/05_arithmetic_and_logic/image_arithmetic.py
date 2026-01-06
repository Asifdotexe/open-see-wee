import cv2 as cv

image1 = cv.imread(r'..\image\binary_one.png')
image2 = cv.imread(r'..\image\binary_two.png')

# resizing the image
height, width, channels = image1.shape
image2_resized = cv.resize(image2, (width, height))

sum_image = cv.add(image1, image2_resized)
cv.imwrite(r'..\image\sum_image.png', sum_image)

# adding color images
image_color1 = cv.imread(r'..\image\shinchan.png')
image_color2 = cv.imread(r'..\image\okay.jpg')

height, width, channels = image_color1.shape
image_color2_resized = cv.resize(image_color2, (width, height))
sum_image_colored = cv.add(image_color1, image_color2_resized)
cv.imwrite(r'..\image\sum_image_colored.png', sum_image_colored)



