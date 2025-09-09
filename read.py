import cv2 as cv

# Reading Images
# img = cv.imread('./Photos/cats.jpg')
# cv.imshow('Cats', img)

# cv.waitKey(0) # Waits indefinitely until a key is pressed

# Reading Videos
capture = cv.VideoCapture('./Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()

    # if `isTrue` is false (the frame could not be read, or we're at the end of the video), we immediately break from the loop
    if isTrue:    
        cv.imshow('Video', frame)
        if cv.waitKey(20) & 0xFF==ord('d'):
            break            
    else:
        break

capture.release()
cv.destroyAllWindows()



