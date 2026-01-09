import cv2 as cv
import os

image = cv.imread(r'..\..\image\bitmap.bmp')

cv.imwrite(r'../../image/bitmap_lossless_compressed_jpeg.jpg',image)
cv.imwrite(r'../../image/bitmap_lossless_compressed_png.png',image)
cv.imwrite(r'../../image/bitmap_lossless_compressed_tiff.tiff',image)

original_size = os.path.getsize(r'..\..\image\bitmap.bmp')
lossless_png_size = os.path.getsize(r'../../image/bitmap_lossless_compressed_png.png')
lossy_jpeg_size = os.path.getsize(r'../../image/bitmap_lossless_compressed_jpeg.jpg')
lossy_tiff_size = os.path.getsize(r'../../image/bitmap_lossless_compressed_tiff.tiff')

print(f"[Size in Bytes]\nOriginal Size: {original_size}\nLossless PNG Size: {lossless_png_size}\nLossy JPEG Size: {lossy_jpeg_size}\nLossy TIFF Size: {lossy_tiff_size}")
