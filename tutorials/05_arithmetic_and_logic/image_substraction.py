
import cv2 as cv

image1 = cv.imread('../../image/binary_one.png')
image2 = cv.imread('../../image/binary_two.png')

height, width = image1.shape[:2]
image2_resized = cv.resize(image2, (width, height))

# substracting image
output_image = cv.subtract(image1, image2_resized)
cv.imwrite('../../image/substracted_image_colored.png', output_image)

#RGB image
image_color1 = cv.imread('../../image/shinchan.png')
image_color2 = cv.imread('../../image/okay.jpg')

height, width = image_color1.shape[:2]
image_color2_resized = cv.resize(image_color2, (width, height))

# blue1 = image_color1[:,:,0]
# green1 = image_color1[:,:,1]
# red1 = image_color1[:,:,2]

# blue2 = image_color2[:,:,0]
# green2 = image_color2[:,:,1]
# red2 = image_color2[:,:,2]

# substracting image
output_image = cv.subtract(image_color1, image_color2_resized)
cv.imwrite('../../image/output_image_substraction_rgb.png', output_image)