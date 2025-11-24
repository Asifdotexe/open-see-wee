"""
Demonstrates how to add two images together using OpenCV's cv.add() function.

[Problem Solved]
This operation allows you to combine two images, increasing the overall brightness or merging features.
OpenCV's cv.add() is a "saturated" operation, meaning pixel values won't wrap around (e.g., 250 + 20 = 255, not 15).

[When to Use]:
- To blend two images or overlays (e.g., adding a watermark).
- To increase the brightness of an image by adding a constant value.
-  As a basic step in more complex image processing pipelines.

[Example Use Case]:
Creating a "double exposure" effect, or overlaying a semi-transparent logo onto a base image
(often used with cv.addWeighted).
"""

import os

import cv2 as cv
import numpy as np

from utils import resize_to_match


def main():
    """
    Demonstrates how to add two images together using OpenCV's cv.add() function.
    """
    image_dir = os.path.join("..", "image")
    binary1_path = os.path.join(image_dir, "binary_one.png")
    binary2_path = os.path.join(image_dir, "binary_two.png")

    image1 = cv.imread(binary1_path)
    image2 = cv.imread(binary2_path)

    if image1 is None or image2 is None:
        print(f"Error: Could not read one or more binary images.")
        return

    image2_resized = resize_to_match(image1, image2)
    sum_image = cv.add(image1, image2_resized)



