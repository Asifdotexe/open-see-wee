import cv2 as cv
import numpy as np

image = cv.imread(r'..\..\image\ok.jpg',0)

# for gamma in [0.2, 0.5, 1, 1.5, 1.8]:
gamma_transformation_image_02 = np.array(255 / (image * 255) ** 0.2, dtype= 'uint8')
# gamma_transformation_image_03 = np.array(255 / (image * 255) ** 0.3, dtype= 'uint8')
# gamma_transformation_image_05 = np.array(255 / (image * 255) ** 0.5, dtype= 'uint8')
# gamma_transformation_image_10 = np.array(255 / (image * 255) ** 1.0, dtype= 'uint8')
# gamma_transformation_image_15 = np.array(255 / (image * 255) ** 1.5, dtype= 'uint8')
# gamma_transformation_image_18 = np.array(255 / (image * 255) ** 1.8, dtype= 'uint8')

    
cv.imwrite(r'../../image/ok_gamma_transformed_02.jpg', gamma_transformation_image_02)
# cv.imwrite(r'../../image/ok_gamma_transformed_03.jpg', gamma_transformation_image_03)
# cv.imwrite(r'../../image/ok_gamma_transformed_05.jpg', gamma_transformation_image_05)
# cv.imwrite(r'../../image/ok_gamma_transformed_10.jpg', gamma_transformation_image_10)
# cv.imwrite(r'../../image/ok_gamma_transformed_15.jpg', gamma_transformation_image_15)
# cv.imwrite(r'../../image/ok_gamma_transformed_18.jpg', gamma_transformation_image_18)
