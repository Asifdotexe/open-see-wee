# Computer Vision through OpenCV

Welcome to the **Computer Vision through OpenCV** tutorial! This repository contains a collection of Python scripts and resources designed to teach you the fundamental concepts of Computer Vision using the OpenCV library.

## Project Structure

The tutorials are organized into modules, each focusing on a specific area of Computer Vision.

### [01. Basics & IO](tutorials/01_basics_and_io/README.md)
Learn the essentials: reading images and videos, understanding dimensions, resizing, cropping, and basic geometric transformations like rotation and translation.

### [02. Image Filtering](tutorials/02_image_filtering/README.md)
Explore techniques to enhance images, including blurring, sharpening, and noise reduction using various filters (Gaussian, Median, Bilateral).

### [03. Morphological Transformations](tutorials/03_morphological_transformations/README.md)
Understand morphological operations like Erosion, Dilation, Opening, and Closing, and their applications in image processing.

### [04. Edge Detection](tutorials/04_edge_detection/README.md)
Discover methods to detect edges in images using operators like Canny, Sobel, and Laplacian.

### [05. Arithmetic & Logic](tutorials/05_arithmetic_and_logic/README.md)
Learn how to perform arithmetic (addition, subtraction) and bitwise operations on images, essential for masking and blending.

### [06. Histograms & Intensity Transforms](tutorials/06_histograms_and_intensity_transforms/README.md)
Analyze image histograms and apply intensity transformations like Histogram Equalization and Power Law transforms to adjust contrast and brightness.

### [07. Image Features & Segmentation](tutorials/07_image_features_and_segmentation/README.md)
Dive into advanced topics like image segmentation and feature detection/matching (Harris Corners, ORB, BRISK).

### [08. Video Analysis](tutorials/08_video_analysis/README.md)
Work with video streams: object tracking (CamShift), background subtraction, and video processing.

### [09. Compression](tutorials/09_compression/README.md)
Understand image compression techniques.

## How to Use
1.  Navigate to a module folder (e.g., `tutorials/01_basics_and_io`).
2.  Read the `README.md` to understand the concepts.
3.  Run the Python scripts to see the code in action.
    *   Note: You may need to adjust image paths in the scripts if you run them directly, as the directory structure has changed. Ideally, run scripts from inside their respective folders.

## Requirements
*   Python 3.x
*   OpenCV (`pip install opencv-python`)
*   NumPy (`pip install numpy`)
*   Matplotlib (`pip install matplotlib`)

## Environment Setup

This project uses [Poetry](https://python-poetry.org/) for dependency management which ensures a reproducible environment.

1.  **Install Poetry**: If you haven't already, install Poetry by following the [official guide](https://python-poetry.org/docs/#installation).

2.  **Install Dependencies**: Navigate to the project root and run:
    ```bash
    poetry install
    ```

3.  **Run Scripts**: You can execute scripts within the Poetry environment using `poetry run`. For example:
    ```bash
    poetry run python tutorials/01_basics_and_io/image_rotation.py
    ```
    Alternatively, spawn a shell within the environment:
    ```bash
    poetry shell
    python tutorials/01_basics_and_io/image_rotation.py
    ```