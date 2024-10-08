import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

image1 = cv.imread('D:\Personal\Github\open-see-wee\image\coins_image.jpg')
image2 = cv.imread('D:\Personal\Github\open-see-wee\image\ok.jpg')
hand = cv.imread(r'D:\Personal\Github\open-see-wee\image\binary_one.png')
rice = cv.imread(r'D:\Personal\Github\open-see-wee\image\binary_two.png')

# resize
print(image1.shape)
print(image2.shape)
height, width, dimensions = image1.shape
image2_resized = cv.resize(image2, (width, height))

print(image2_resized.shape)

# add two images
image3 = cv.add(image1,image2_resized)

# substract two images
image4 = cv.subtract(image1,image2_resized)

# image blending
alpha = 0.3
beta = 0.7
gamma = 0
image5 = cv.addWeighted(image1, alpha, image2_resized, beta, gamma)

# image rotation
# you can do rotation in the following ways:
# cv.ROTATE_CLOCKWISE_90
# cv.ROTATE_COUNTERCLOCKWISE_90
rotated_ok = cv.rotate(image2, cv.ROTATE_180)

# image translation (low chance aane ka)
height, width, _ = image2.shape
matrix = np.float32(
    [
        [1,0,100],
        [0,1,100]
    ]
)
translated_ok = cv.warpAffine(image2, matrix, (height, width))

# # image scaling
# ratio = 50.0 / image2.shape[0]
# dim = (int(image2[1]*ratio),50)
# scale_image = cv.resize(image2, dim, interpolation=cv.INTER_AREA)

# erode

coin = cv.imread(r'D:\Personal\Github\open-see-wee\image\coins_image.jpg')

kernal = np.ones((9,9), dtype='uint8')
erosion_coin = cv.erode(coin, kernal, iterations=10)

# dilate

dilation_coin = cv.dilate(coin, kernal, iterations=10)

# opening

opening_coin = cv.morphologyEx(coin, cv.MORPH_OPEN, kernal, iterations=5)

# closing 

closing_coin = cv.morphologyEx(coin, cv.MORPH_CLOSE, kernal, iterations=5)

# top hat

top_hat_coin = cv.morphologyEx(coin, cv.MORPH_TOPHAT, kernal, iterations=15)

black_hat_coin = cv.morphologyEx(coin, cv.MORPH_BLACKHAT, kernal, iterations=10)

# morph gradient
morph_gradient_coin = cv.morphologyEx(coin, cv.MORPH_GRADIENT, kernal, iterations=2)

# edge detection (canny)
flag = cv.imread(r'D:\Personal\Github\open-see-wee\image\flag_multiple.jpg')
flag_edge_canny = cv.Canny(flag, threshold1=100, threshold2=200)
coin_edge_canny = cv.Canny(coin, threshold1=100, threshold2=200)

# edge detection (laplacian)
flag_edge_laplacian = cv.Laplacian(flag, cv.CV_64F)

# edge detection (sobel)
flag_edge_sobel = cv.Sobel(flag, cv.CV_64F, dx=1, dy=1, ksize=3)

# blurring
# the kernal should be divided by the square of the kernal i.e. if kernal is 7,7 then 
# you need to divide it by 7*7 i.e 49
blur_flag = cv.filter2D(flag, ddepth=-1, kernel=kernal/81)

# gaussian blur 
gaussian_flag = cv.GaussianBlur(flag, ksize=(7,7), sigmaX=0, sigmaY=0)

# median blur
median_flag = cv.medianBlur(flag, ksize=5)

# bilateral blur
bilteral_flag = cv.bilateralFilter(flag, d=20, sigmaColor=255, sigmaSpace=255)

# sharpening blur
sharpenKernal = np.array(
    [
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0]
    ]
)

flag_sharpen = cv.filter2D(flag, ddepth=-1, kernel=sharpenKernal)
coin_sharpen = cv.filter2D(coin, ddepth=-1, kernel=sharpenKernal)

# embossing

emboss_kernal = np.array(
    [
        [0, 0, -1],
        [0, 0, 0],      
        [1, 0, 0]
    ]
)

embossed_coin = cv.filter2D(coin, ddepth=-1, kernel=emboss_kernal)

# flipping

height, width, _ = image2.shape
flipKernal = np.float32(
    [
        [1,0,0],
        [0, -1, height],
        [0, 0, 1]
    ]
)

ok_flipped = cv.warpPerspective(image2, flipKernal, (int(width), int(height)))

# extracting BGR channels from image
blue, green, red = cv.split(flag)
print("Blue value:",blue,"\n","Green value:", green,"\n", "Red value:", red)

# creating histogram
histogram = cv.calcHist([flag], [0], None,[255], [0,255])
plt.plot(histogram)
plt.savefig(r'D:\Personal\Github\open-see-wee\practice-output\Q1\flag_histogram_blue.png')

# equalized histograms
flag_gray = cv.cvtColor(flag, cv.COLOR_BGR2GRAY)
eq_hist = cv.equalizeHist(flag_gray)
plt.savefig(r'D:\Personal\Github\open-see-wee\practice-output\Q1\flag_histogram_equalized.png')

# bitwise not
not_hand = cv.bitwise_not(hand, mask=None)

# bitwise and
h, w, _ = hand.shape
rice_resized = cv.resize(rice, (w,h))
and_hand_rice = cv.bitwise_and(hand,rice_resized, mask=None)

# bitwise or
or_hand_rice = cv.bitwise_or(hand, rice_resized, mask=None)

# bitwise xor
xor_hand_rice = cv.bitwise_xor(hand, rice_resized, mask=None)

# power law transformation
gamma = 1.0
flag_gamma_transformation = np.array(255 / (flag ** gamma), dtype='uint8')

cv.imwrite('D:\Personal\Github\open-see-wee\practice-output\Q1\coin_okay_add.png', image3)
cv.imwrite('D:\Personal\Github\open-see-wee\practice-output\Q1\coin_okay_substract.png', image4)
cv.imwrite('D:\Personal\Github\open-see-wee\practice-output\Q1\coin_okay_blending.png', image5)
cv.imwrite(r'D:\Personal\Github\open-see-wee\practice-output\Q1\rotated_ok.png', rotated_ok)
cv.imwrite(r'D:\Personal\Github\open-see-wee\practice-output\Q1\translation_ok.png', translated_ok)
cv.imwrite(r'D:\Personal\Github\open-see-wee\practice-output\Q1\erosion_coin.png', erosion_coin)
cv.imwrite(r'D:\Personal\Github\open-see-wee\practice-output\Q1\dilation_coin.png', dilation_coin)
cv.imwrite(r'D:\Personal\Github\open-see-wee\practice-output\Q1\opening_coin.png', opening_coin)
cv.imwrite(r'D:\Personal\Github\open-see-wee\practice-output\Q1\closing_coin.png', closing_coin)
cv.imwrite(r'D:\Personal\Github\open-see-wee\practice-output\Q1\top_hat_coin.png', top_hat_coin)
cv.imwrite(r'D:\Personal\Github\open-see-wee\practice-output\Q1\black_hat_coin.png', black_hat_coin)
cv.imwrite(r'D:\Personal\Github\open-see-wee\practice-output\Q1\morph_gradient_coin.png', morph_gradient_coin)
cv.imwrite(r'D:\Personal\Github\open-see-wee\practice-output\Q1\flag_edge_canny.png', flag_edge_canny)
cv.imwrite(r'D:\Personal\Github\open-see-wee\practice-output\Q1\coin_edge_canny.png', coin_edge_canny)
cv.imwrite(r'D:\Personal\Github\open-see-wee\practice-output\Q1\flag_edge_laplacian.png', flag_edge_laplacian)
cv.imwrite(r'D:\Personal\Github\open-see-wee\practice-output\Q1\flag_edge_sobel.png', flag_edge_sobel)
cv.imwrite(r'D:\Personal\Github\open-see-wee\practice-output\Q1\blur_flag.png', blur_flag)
cv.imwrite(r'D:\Personal\Github\open-see-wee\practice-output\Q1\gaussian_flag.png', gaussian_flag)
cv.imwrite(r'D:\Personal\Github\open-see-wee\practice-output\Q1\median_flag.png', median_flag)
cv.imwrite(r'D:\Personal\Github\open-see-wee\practice-output\Q1\bilteral_flag.png', bilteral_flag)
cv.imwrite(r'D:\Personal\Github\open-see-wee\practice-output\Q1\flag_sharpen.png', flag_sharpen)
cv.imwrite(r'D:\Personal\Github\open-see-wee\practice-output\Q1\coin_sharpen.png', coin_sharpen)
cv.imwrite(r'D:\Personal\Github\open-see-wee\practice-output\Q1\embossed_coin.png', embossed_coin)
cv.imwrite(r'D:\Personal\Github\open-see-wee\practice-output\Q1\ok_flipped.png', ok_flipped)
cv.imwrite(r'D:\Personal\Github\open-see-wee\practice-output\Q1\not_hand.png', not_hand)
cv.imwrite(r'D:\Personal\Github\open-see-wee\practice-output\Q1\and_hand_rice.png', and_hand_rice)
cv.imwrite(r'D:\Personal\Github\open-see-wee\practice-output\Q1\or_hand_rice.png', or_hand_rice)
cv.imwrite(r'D:\Personal\Github\open-see-wee\practice-output\Q1\xor_hand_rice.png', xor_hand_rice)
cv.imwrite(r'D:\Personal\Github\open-see-wee\practice-output\Q1\flag_gamma_transformation.png', flag_gamma_transformation)
print("Done!")