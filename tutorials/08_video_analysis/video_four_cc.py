import cv2 as cv

# Open the video file
from pathlib import Path
base_dir = Path(__file__).resolve().parent.parent.parent
video_path = str(base_dir / 'video' / 'tracking.mp4')
capture = cv.VideoCapture(video_path)

# Define the codec and create VideoWriter object
fourcc = cv.VideoWriter_fourcc(*"mp4v")

# Check if the video was successfully opened
if not capture.isOpened():
    print("Error: Unable to open video file.")
else:
    # Read the first frame to get dimensions
    ret, frame = capture.read()
    if ret:
        # Get original frame dimensions
        width = frame.shape[1]
        height = frame.shape[0]

        # Scale down by 50%
        scale_percent = 50
        new_width = int(width * scale_percent / 100)
        new_height = int(height * scale_percent / 100)
        dimensions = (new_width, new_height)

        # Initialize the video writer with the new dimensions
        output_path = str(base_dir / 'video' / 'tracking_resized.mp4')
        output_video = cv.VideoWriter(output_path, fourcc, 30, dimensions)

        while True:
            # Read frame by frame
            ret, frame = capture.read()
            if not ret:
                break  # Break if no more frames

            # Resize the frame
            resized_frame = cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

            # Write the resized frame to the output video
            output_video.write(resized_frame)

            # Display the frame (optional)
            cv.imshow("Resized Frame", resized_frame)
            
            # Press 'q' to exit the display window
            if cv.waitKey(30) & 0xFF == ord('q'):
                break

        # Release resources
        capture.release()
        output_video.release()
        cv.destroyAllWindows()
    else:
        print("Error: Unable to read frames from video.")