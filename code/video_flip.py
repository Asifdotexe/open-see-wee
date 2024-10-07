import cv2 as cv

video = cv.VideoCapture(r'../video/tracking.mp4')
ret, frame = video.read()

if not ret:
    print("Error: Unable to read the video frame.")
else:

    flip_horizontal = cv.flip(frame, 1)
    flip_vertical = cv.flip(frame, 0)
    flip_both = cv.flip(frame, -1)

    # Show the original and flipped frames
    cv.imshow("Original", frame)
    cv.imshow("Horizontal", flip_horizontal)
    cv.imshow("Vertical", flip_vertical)
    cv.imshow("Both", flip_both)

    cv.waitKey(0)
    
video.release()
cv.destroyAllWindows()