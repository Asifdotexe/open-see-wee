import cv2 as cv
import numpy as np

image1 = cv.imread('../image/luffy.jpg')
image2 = cv.imread('../image/flag.png')

gray1 = cv.cvtColor(image1,cv.COLOR_BGR2GRAY)
gray2 = cv.cvtColor(image2,cv.COLOR_BGR2GRAY)

orb = cv.ORB_create()

#Find key-points and descriptions in both images
keypoints1, descriptors1 = orb.detectAndCompute(gray1,None)
keypoints2, descriptors2 = orb.detectAndCompute(gray2,None)

#Find best detected features using Brute Force Matcher and match according to hamming distance

bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)
number_of_matches = bf.match(descriptors1,descriptors2)
number_of_matches = sorted(number_of_matches,key=lambda x:x.distance)
total_feature_count = len(number_of_matches)

print(f"Total number of features : {total_feature_count}")

output = cv.drawMatches(gray1,keypoints1,gray2,keypoints2,number_of_matches[:30]
                        ,None,flags=2)

cv.imwrite('../image/luffy_flag_feature_matching.png', output)