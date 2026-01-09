import cv2 as cv
image = cv.imread('../../image/luffy.jpg')
image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# apply binary thresholding
ret, threshold_image = cv.threshold(image_gray, 150, 200, cv.THRESH_BINARY)
cv.imwrite('../../image/luffy_segmentation_threshold.png', threshold_image)
# display the threshold image
# detect contours on the binary image
contours, hierarchy = cv.findContours(
    image=threshold_image, mode=cv.RETR_TREE, method=cv.CHAIN_APPROX_NONE
)

image_copy = image.copy()
output = cv.drawContours(
    image=image_copy, contours=contours, contourIdx=-1, color=(0, 255, 0), 
    thickness=2, lineType=cv.LINE_AA
)

cv.imwrite('../../image/luffy_segmentation_output.png', output)