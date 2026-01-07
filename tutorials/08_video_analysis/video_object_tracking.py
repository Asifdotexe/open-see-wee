import cv2
import numpy as np

# Load the video
capture = cv2.VideoCapture(r"..\..\video\tracking.mp4")

# Read the first frame
ret, frame = capture.read()

# Set up the initial tracking window
x, y, w, h = 300, 200, 100, 50
track_window = (x, y, w, h)

# Define the region of interest (ROI) for tracking
roi = frame[y:y+h, x:x+w]

# Convert the ROI to HSV color space
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

# Create a mask to ignore low-light pixels
mask = cv2.inRange(hsv_roi, np.array((0., 60., 32.)), np.array((180., 255., 255.)))

# Calculate the histogram for the region of interest
roi_hist = cv2.calcHist([hsv_roi], [0], mask, [180], [0, 180])

# Normalize the histogram
cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)

# Define the termination criteria: 10 iterations or moving by at least 1 pt
term_criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)

while True:
    ret, frame = capture.read()
    
    if ret:
        # Convert the current frame to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        # Backproject the model histogram roi_hist onto the current frame
        dst = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)
        
        # Apply the MeanShift algorithm to find the new location of the object
        ret, track_window = cv2.meanShift(dst, track_window, term_criteria)
        
        # Draw the tracking window on the frame
        x, y, w, h = track_window
        result_frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
        # Display the result
        cv2.imshow("Tracking", result_frame)
        
        # Exit when 'ESC' key is pressed
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
    else:
        break

# Release the capture and close windows
capture.release()
cv2.destroyAllWindows()