import cv2 as cv

from pathlib import Path
video_path = str(Path(__file__).resolve().parent.parent.parent / 'video' / 'tracking.mp4')
video = cv.VideoCapture(video_path)
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