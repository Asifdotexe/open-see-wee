import cv2 as cv
import numpy as np

image = cv.imread('image\meme.jpeg')

dimension = image.shape
print(dimension)

# splitting image as 3 channels
blue = image[:,:,0]
green = image[:,:,1]
red = image[:,:,2]