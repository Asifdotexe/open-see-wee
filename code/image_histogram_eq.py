import cv2 as cv

import numpy as np

image = cv.imread(r'..\image\ok.jpg', cv.IMREAD_GRAYSCALE)

histogram_eq_image = cv.equalizeHist(image)

cv.imshow("Original Image",image)
cv.waitKey(0)
cv.destroyAllWindows()

cv.imshow("Equalized histogram",histogram_eq_image)
cv.waitKey(0)
cv.destroyAllWindows()