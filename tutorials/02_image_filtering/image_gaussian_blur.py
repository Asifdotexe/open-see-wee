import cv2 as cv

image1 = cv.imread(r'..\..\image\noisy_women.jpg')
image2 = cv.imread(r'..\..\image\noisy_rat.jpg')

# sigma x and sigma y are the gaussian kernal standard deviation in horizontal and vertical direction, if set to 0, standard deviation are computed fromm kernal width and kernal height respectively.
gaussian_blur_women = cv.GaussianBlur(src=image1, ksize=(5,5), sigmaX=0, sigmaY=0,)
gaussian_blur_women_g1 = cv.GaussianBlur(src=image1, ksize=(5,5), sigmaX=1, sigmaY=1)
gaussian_blur_rat = cv.GaussianBlur(src=image2, ksize=(15,15), sigmaX=0, sigmaY=0,)

cv.imwrite(r'..\..\image\noisy_women_gaussian_blurred.png', gaussian_blur_women)
cv.imwrite(r'..\..\image\noisy_women_gaussian_blurred_sigmas_1.png', gaussian_blur_women_g1)
cv.imwrite(r'..\..\image\noisy_rat_gaussian_blurred.png', gaussian_blur_rat)