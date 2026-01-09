import cv2 as cv
import numpy as np

from pathlib import Path

base_dir = Path(__file__).resolve().parent.parent.parent
image1_path = str(base_dir / 'image' / 'shinchan.png')
image2_path = str(base_dir / 'image' / 'ok.jpg')

image1 = cv.imread(image1_path)
image2 = cv.imread(image2_path)

if image1 is None:
    raise FileNotFoundError(f"Failed to load image1 from {image1_path}")
if image2 is None:
    raise FileNotFoundError(f"Failed to load image2 from {image2_path}")

height, width = image1.shape[:2]
image2_resized = cv.resize(image2, (width, height))

b1, g1, r1 = cv.split(image1)
b2, g2, r2 = cv.split(image2_resized)

b_xor = cv.bitwise_xor(b1, b2)
g_xor = cv.bitwise_xor(g1, g2)
r_xor = cv.bitwise_xor(r1, r2)
xor_image = cv.merge([b_xor, g_xor, r_xor])
output_path = str(base_dir / 'image' / 'bitwise_xor_rgb.jpg')
if not cv.imwrite(output_path, xor_image):
    raise RuntimeError(f"Failed to write image to {output_path}")
