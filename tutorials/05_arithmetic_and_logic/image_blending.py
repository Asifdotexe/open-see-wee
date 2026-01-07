import cv2 as cv

image1 = cv.imread(r'..\..\image\binary_one.png')
image2 = cv.imread(r'..\..\image\binary_two.png')

height, width = image1.shape[:2]
image2_resized = cv.resize(image2, (width, height))

alpha = 0.7
beta = 0.3
gamma = 0.5

# adding weights
output_image = cv.addWeighted(image1, alpha, image2_resized, beta, gamma)
cv.imwrite(r'../../image/output_image_blending_gamma_point_5.png', output_image)