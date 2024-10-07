import cv2 as cv

print("[Code running]")
video = cv.VideoCapture(r'../video/tracking.mp4')

while True:
    ret, frame = video.read()
    if not ret: break   
    cv.imshow("Frame", frame)
    
    if cv.waitKey(0) & 0xFF: break

video.release()
cv.destroyAllWindows()

print("[Stop running]")
