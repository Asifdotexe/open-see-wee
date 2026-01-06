# Video Analysis

Processing video streams, tracking objects, and background subtraction.

## Concepts Covered

*   **Video IO**: Reading from camera or file, and writing video.
*   **Object Tracking**:
    *   **CamShift (Continuously Adaptive Mean Shift)**: An object tracking algorithm based on mean shift. It finds the object center and orientation.
*   **Background Subtraction**: Separating foreground objects from the background.

## Scripts

*   `video_cam_shift.py`: Implements CamShift tracking.
*   `video_object_tracking.py`: Tracking objects based on color (HSV).
*   `video_background_subtractor.py`: Removes background.
*   `video_flip.py`: Flipping video.
*   (Basic video reading is covered in [Module 01](../01_basics_and_io/README.md))
