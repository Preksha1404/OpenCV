import cv2 as cv
import numpy as np

# Create blank image
blank=np.zeros((500,500,3),dtype='uint8') # Give height, width and color channels
# cv.imshow('Blank',blank)

# Print shape of blank image
# print(blank.shape)

# Paint the image a certain color
# blank[:]=0,255,0 # Green
# cv.imshow('Green',blank)
# blank[200:300,300:400]=255,0,0 # Blue square
# cv.imshow('Blue',blank)

# Draw a rectangle
# cv.rectangle(blank,(0,0),(250,250),(255,0,0),thickness=2)
# cv.rectangle(blank,(0,0),(250,250),(0,255,0),thickness=cv.FILLED) # Filled rectangle
cv.rectangle(blank,(blank.shape[1]//2,blank.shape[0]//2),(500,500),(0,0,255),thickness=-1) # Red rectangle
cv.imshow('Rectangle',blank)

# Draw a circle
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,255,0),thickness=-1) # Green filled circle
cv.imshow('Circle',blank)

# Draw a line
cv.line(blank,(blank.shape[1]//2,blank.shape[0]//2),(500,500),(255,255,255),thickness=3) # White line
cv.imshow('Line',blank)

# Write text
cv.putText(blank,'Hello World',(0,225),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,0,255),thickness=2) # Red text
cv.imshow('Text',blank)

cv.waitKey(0)