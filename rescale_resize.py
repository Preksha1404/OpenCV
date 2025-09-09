import cv2 as cv    

# Rescale the frame of video or image by scaling factor
def rescaleFrame(frame, scale=0.25):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# Change the resolution of live video
def changeRes(width,height):
    # Live video
    capture.set(3,width) 
    capture.set(4,height)

# Reading Image
# img = cv.imread('./Photos/cat.jpg')
# cv.imshow('Cat', img)
# cv.imshow('Cat Resized', rescaleFrame(img))
# cv.waitKey(0) # Waits indefinitely until a key is pressed

# Reading Video
capture = cv.VideoCapture('./Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)
    
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()