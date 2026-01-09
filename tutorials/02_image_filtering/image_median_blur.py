import cv2 as cv

image1 = cv.imread('../../image/noisy_women.jpg')
image2 = cv.imread('../../image/noisy_rat.jpg')
image3 = cv.imread('../../image/noisy_parrot.jpg')

median_blur_women = cv.medianBlur(src=image1, ksize=5)
median_blur_rat = cv.medianBlur(src=image2, ksize=15)
median_blur_parrot = cv.medianBlur(src=image3, ksize=7)

cv.imwrite('../../image/noisy_women_median_blurred.png', median_blur_women)
cv.imwrite('../../image/noisy_rat_median_blurred.png', median_blur_rat)
cv.imwrite('../../image/noisy_parrot_median_blurred.png', median_blur_parrot)