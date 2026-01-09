import cv2 as cv
from matplotlib import pyplot as plt

image = cv.imread("../../image/coins_image.jpg")
if image is None:
    raise RuntimeError("Failed to load image from ../../image/coins_image.jpg")

orb = cv.ORB_create()
keypoints = orb.detect(image, None)

keypoints, descriptors = orb.compute(image, keypoints)

imageKP = cv.drawKeypoints(image, keypoints, None, color = (0,255,0),flags = 0)
plt.imshow(imageKP),plt.show()
