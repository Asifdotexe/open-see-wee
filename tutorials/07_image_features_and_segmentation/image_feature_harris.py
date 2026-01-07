import cv2 as cv

# Read the image in BGR format (default behavior)
image = cv.imread(r"..\..\image\coins_image.jpg")

# Detect corners using the grayscale version of the image
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY).astype('float32')
corners = cv.cornerHarris(gray, 2, 3, 0.04)

# Mark corners in the original BGR image
image[corners > 0.01 * corners.max()] = [0, 0, 255]

cv.imwrite(r"..\..\image\coins_harris_features.png", image)