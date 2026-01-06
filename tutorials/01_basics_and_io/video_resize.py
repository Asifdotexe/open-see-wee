import cv2 as cv

capture = cv.VideoCapture(r'../video/tracking.mp4')

while True:
    ret, frame = capture.read()
    if not ret:
        break
    
    width = frame.shape[1]
    height = frame.shape[0]
    scale_percent = 150
    
    new_width = int(width * scale_percent/100)
    new_height= int(height * scale_percent/100)
    
    dimension = (new_width, new_height)
    
    resize_area = cv.resize(frame, dimension,interpolation=cv.INTER_AREA)
    resize_linear = cv.resize(frame, dimension,interpolation=cv.INTER_LINEAR)
    resize_cubic = cv.resize(frame, dimension,interpolation=cv.INTER_CUBIC)
    
    cv.imshow("Original", frame)
    cv.imshow("Resized Area", resize_area)
    cv.imshow("Resized Linear", resize_linear)
    cv.imshow("Resized Cubic", resize_cubic)
    
    cv.waitKey(1)
    if (cv.waitKey(1) == 32):
        break
    
capture.release()
cv.destroyAllWindows()