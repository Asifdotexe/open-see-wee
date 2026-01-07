import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

image = cv.imread(r'..\..\image\ok.jpg')

histogram = cv.calcHist([image], [0], None, [256], [0,256])
plt.plot(histogram)
plt.xlim([0,256])
plt.show()