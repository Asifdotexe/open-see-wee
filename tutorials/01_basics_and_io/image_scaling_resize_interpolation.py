import cv2 as cv

image = cv.imread(r'..\image\ok.jpg')

ratio = 50.0/image.shape[0] # # 50% percent, shape[0] is the height
dim = (int(image.shape[1]* ratio),50)
scaled_image = cv.resize(image,dim,interpolation= cv.INTER_AREA)

cv.imwrite(r'..\image\ok_resized_scaled.jpg', scaled_image)