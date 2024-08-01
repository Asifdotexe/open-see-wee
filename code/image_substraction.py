import cv2 as cv

image1 = cv.imread(r'..\image\binary_one.png')
image2 = cv.imread(r'..\image\binary_two.png')

height, width = image1.shape[:2]
image2_resized = cv.resize(image2, (width, height))

# substracting image
output_image = cv.subtract(image1, image2_resized)
cv.imwrite(r'..\image\output_image_substraction.png', output_image)

#RGB image
image1_rgb = cv.imread(r'..\image\okay.jpg')
image2_rgb = cv.imread(r'..\image\meme.jpeg')

height, width = image1_rgb.shape[:2]
image2_resized_rgb = cv.resize(image2_rgb, (width, height))

# blue1 = image1[:,:,0]
# green1 = image1[:,:,1]
# red1 = image1[:,:,2]

# blue2 = image2[:,:,0]
# green2 = image2[:,:,1]
# red2 = image2[:,:,2]

# substracting image
output_image = cv.subtract(image1_rgb, image2_resized_rgb)
cv.imwrite(r'..\image\output_image_substraction_rgb.png', output_image)