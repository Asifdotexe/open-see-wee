import cv2 as cv
import numpy as np

grid = 7
image = cv.imread('../../image/luffy.jpg')

kernel_ellipse = cv.getStructuringElement(cv.MORPH_ELLIPSE, (grid,grid))
kernel_cross = cv.getStructuringElement(cv.MORPH_CROSS, (grid,grid))
kernel_rectangle = cv.getStructuringElement(cv.MORPH_RECT, (grid,grid))

top_hat_ellipse = cv.morphologyEx(image, cv.MORPH_TOPHAT, kernel=kernel_ellipse)
top_hat_cross = cv.morphologyEx(image, cv.MORPH_TOPHAT, kernel=kernel_cross)
top_hat_rectangle = cv.morphologyEx(image, cv.MORPH_TOPHAT, kernel=kernel_rectangle)

black_hat_ellipse = cv.morphologyEx(image, cv.MORPH_BLACKHAT, kernel=kernel_ellipse)
black_hat_cross = cv.morphologyEx(image, cv.MORPH_BLACKHAT, kernel=kernel_cross)
black_hat_rectangle = cv.morphologyEx(image, cv.MORPH_BLACKHAT, kernel=kernel_rectangle)

cv.imwrite('../../image/luffy_top_hat_morphology_ellipse.png', top_hat_ellipse)
cv.imwrite('../../image/luffy_top_hat_morphology_cross.png', top_hat_cross)
cv.imwrite('../../image/luffy_top_hat_morphology_rectangle.png', top_hat_rectangle)

cv.imwrite('../../image/luffy_black_hat_morphology_ellipse.png', black_hat_ellipse)
cv.imwrite('../../image/luffy_black_hat_morphology_cross.png', black_hat_cross)
cv.imwrite('../../image/luffy_black_hat_morphology_rectangle.png', black_hat_rectangle)