import cv2 as cv

# reading a colored image
image = cv.imread('image\meme.jpeg')

# storing the properties of the image
dimension = image.shape
height = image.shape[0]
width = image.shape[1]
channel = image.shape[2]

# printing the properties of the image
print('dimension:', dimension,'height:', height, 'width:', width, 'channel:', channel)

# reading a black and white image
image_bw = cv.imread('image\cheetah_bw.jpeg')

dimension_bw = image_bw.shape
height_bw = image_bw.shape[0]
width_bw = image_bw.shape[1]
channel_bw = image_bw.shape[2]

# printing the properties of the image
print('dimension:', dimension_bw,'height:', height_bw, 'width:', width_bw, 'channel:', channel_bw)

image_grayscale = cv.imread('image\ok.jpg', cv.IMREAD_GRAYSCALE)

dimension = image_grayscale.shape
height = image_grayscale.shape[0]
width = image_grayscale.shape[1]
channel = image_grayscale.shape[2]

# printing the properties of the image
print('dimension:', dimension,'height:', height, 'width:', width, 'channel:', channel)


