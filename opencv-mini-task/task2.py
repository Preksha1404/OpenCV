import cv2 as cv
import numpy as np

img=cv.imread('../Photos/Shapes.png')
cv.imshow('Shapes',img)


# Blur Image
blur=cv.GaussianBlur(img,(9,9),0)
cv.imshow('Blurred Image',blur)


# Edge Detection
canny=cv.Canny(blur,145,175)
cv.imshow('Canny Image',canny)


# Dilated Image
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('Dilated', dilated)


# Eroding
eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow('Eroded', eroded)


# Boundaries of Image
blank = np.zeros(img.shape, dtype='uint8')

contours, hierarchies=cv.findContours(canny,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE) # Take edges, mode, approximation method
print(f'{len(contours)} contours found!')

cv.drawContours(blank,contours, -1, (255,0,255), 1)
cv.imshow('Contours Drawn', blank)


# Draw a rectangle on the detected image
objects=img.copy()
for cnt in contours:
    x,y,w,h = cv.boundingRect(cnt)
    objects=cv.rectangle(objects,(x,y),(x+w,y+h),(0,255,255),2)
cv.imshow('Rectangle on objects',objects)


# Crop the image of detected objects
for i, cnt in enumerate(contours):
    x, y, w, h = cv.boundingRect(cnt)
    cropped = img[y:y+h, x:x+w]
    cv.imshow(f'Cropped Object{i+1}', cropped) # Show only last cropped object


# Split all three bands of the image without using cv2
# OpenCV uses BGR format
blue  = img[:, :, 0]
green = img[:, :, 1]
red   = img[:, :, 2]

cv.imshow('Blue Image',blue)
cv.imshow('Green Image',green)
cv.imshow('Red Image',red)


# Add black and white border padding to the image and display
# Add black border
black_border = cv.copyMakeBorder(img, 20, 20, 20, 20,borderType=cv.BORDER_CONSTANT,value=(0, 0, 0))

# Add white border
white_border = cv.copyMakeBorder(img, 20, 20, 20, 20,borderType=cv.BORDER_CONSTANT,value=(255, 255, 255))

cv.imshow("Black Border", black_border)
cv.imshow("White Border", white_border)

cv.waitKey(0)