import cv2 as cv
import numpy as np

image = cv.imread(r'..\..\image\ok.jpg')
elgato = cv.imread(r'..\..\image\greyscale_cat.jpg')
shinchan = cv.imread(r'..\..\image\shinchan.png')
rick = cv.imread(r'..\..\image\rickroll.jpg')

kernelSharp = np.array([
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0]
])

sharp_image = cv.filter2D(src=image, ddepth=-1, kernel=kernelSharp)
sharp_elgato = cv.filter2D(src=elgato, ddepth=-1, kernel=kernelSharp)
sharp_shinchan = cv.filter2D(src=shinchan, ddepth=-1, kernel=kernelSharp)
sharp_rick = cv.filter2D(src=rick, ddepth=-1, kernel=kernelSharp)

cv.imwrite(r'../image/ok_sharpened_filter.jpg', sharp_image)
cv.imwrite(r'../image/ok_sharpened_cat.jpg', sharp_elgato)
cv.imwrite(r'../image/ok_sharpened_shinchan.jpg', sharp_shinchan)
cv.imwrite(r'../image/ok_sharpened_rickroll.jpg', sharp_rick)