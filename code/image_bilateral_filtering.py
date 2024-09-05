import cv2 as cv

ok = cv.imread(r'../image/ok.jpg')
rick = cv.imread(r'../image/rickroll.jpg')

bilateral_filter_image = cv.bilateralFilter(src=ok, d=4, sigmaColor= 75, sigmaSpace=75)
bilateral_filter_rick = cv.bilateralFilter(src=rick, d=4, sigmaColor= 75, sigmaSpace=75)
# d represents the diameter of pixel neighborhood for filtering
# sigma color = standard dev. of 1D colour intensity distribution
# sigma space = standard deviation of 2D spatial distribution

cv.imwrite(r'../image/ok_bilteral_filtering.jpg', bilateral_filter_image)
cv.imwrite(r'../image/rick_bilteral_filtering.jpg', bilateral_filter_rick)