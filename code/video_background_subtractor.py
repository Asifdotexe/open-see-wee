import cv2 as cv 
import numpy as np

#fgbg1 = cv.createBackgroundSubtractorMOG()
fgbg2 = cv.createBackgroundSubtractorMOG2()
# fgbg3 = cv.createBackgroundSubtractorGMG()

capture = cv.VideoCapture(0)

while(1):
    ret,image = capture.read()
    # fgmask1 = fgbg1.apply(image)
    fgmask2 = fgbg2.apply(image)
    # fgmask3 = fgbg3.apply(image)

    cv.imshow('original',image)
    # cv.imshow('MOG',fgmask1)
    cv.imshow('MOG2',fgmask2)
    # cv.imshow('GMG',fgmask3)

    k = cv.waitKey(30)&0xff
    if k == 27:
        break

capture.release()
cv.destroyAllWindows()