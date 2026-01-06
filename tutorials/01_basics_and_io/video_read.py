import cv2 as cv

video = cv.VideoCapture(r'../video/tracking.mp4')

width = int(video.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv.CAP_PROP_FRAME_HEIGHT))
fps = video.get(cv.CAP_PROP_FPS)

fourcc = cv.VideoWriter_fourcc(*'mp4v') 
output = cv.VideoWriter(r'../video/output_video.mp4', fourcc, fps, (width, height))

while True:
    ret, frame = video.read()
    if not ret: 
        break

    output.write(frame)

video.release()
output.release()