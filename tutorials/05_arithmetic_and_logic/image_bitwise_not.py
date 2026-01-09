import cv2 as cv

from pathlib import Path

base_dir = Path(__file__).resolve().parent.parent.parent
image1_path = str(base_dir / 'image' / 'binary_one.png')
image2_path = str(base_dir / 'image' / 'binary_two.png')

image1 = cv.imread(image1_path)
image2 = cv.imread(image2_path)

if image1 is None:
    raise FileNotFoundError(f"Failed to load image1 from {image1_path}")
if image2 is None:
    raise FileNotFoundError(f"Failed to load image2 from {image2_path}")

height, width = image1.shape[:2]
image2_resized = cv.resize(image2, (width, height))

not_image1 = cv.bitwise_not(image1, mask=None)
not_image2 = cv.bitwise_not(image2_resized, mask=None)
output_path1 = str(base_dir / 'image' / 'bitwise_not_binary_one.jpg')
output_path2 = str(base_dir / 'image' / 'bitwise_not_binary_two.jpg')

cv.imwrite(output_path1, not_image1)
cv.imwrite(output_path2, not_image2)
