import cv2 as cv
import numpy as np

image = cv.imread(r'..\image\ok.jpg')

dimension = image.shape
height = image.shape[0]
width = image.shape[1]
channel = image.shape[2]

print(channel)

# splitting image as 3 channels
blue = image[:,:,0]
green = image[:,:,1]
red = image[:,:,2]

print(blue, green, red)