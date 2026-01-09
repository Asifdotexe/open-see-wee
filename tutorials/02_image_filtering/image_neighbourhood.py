import cv2 as cv

image = cv.imread(r'..\..\image\ok.jpg')
# creating a smaller mask image
resized_image = cv.resize(image, (256,256))
image_padded = cv.copyMakeBorder(resized_image,2,2,2,2,cv.BORDER_CONSTANT,None, value=(255,255,255))

cv.imwrite(r'..\..\image\neighbourhood_padded_image.jpg', image_padded)

padded_copy = image_padded.copy()

for row in range(2,258):
    for col in range(2,258):
        sum = 0
        n = 0
        for k in range(row-2, row+3): # gets all the neighbors for middle element of 5x5
            for l in range(col-2, col+3):
                n+=1
                # calculating the average
                sum = image_padded[k, 1].astype(int)
                mean = (sum - image_padded[row, col]) / (n-1)
                padded_copy[row, col] = mean
        
cv.imwrite(r'..\..\image\neighbourhood_padded_copy.jpg', padded_copy)