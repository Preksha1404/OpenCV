
import cv2 as cv
import numpy as np

img = cv.imread('../Photos/cats.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)


# Identify contours --> 
# 1. Detect Edge using canny and then use findContours
# 2. Binarize image using thresholding and then use findContours

# Change image color form BGR to GRAY
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blur image
blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge detection
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny Edges', canny)

# contours --> list of all coordinates of contours present in image
# hierarchies --> hierarchies of shapes in image

# MODES
# RETR_TREE --> if you want all hierarchical contours
# RETR_EXTERNAL --> if you want all external contours
# RETR_LIST --> if you want all contours

#  Approximation Method
# CHAIN_APPROX_NONE --> give all contour coordinates of edges
# CHAIN_APPROX_SIMPLE --> Simplify and give simple one coordinates of contours

contours, hierarchies=cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_NONE) # Take edges, mode, approximation method
print(f'{len(contours)} contour(s) found!')

# Thresholding --> Look Image and binarize the image (If less than threshold set to 0 and black color and otherwise 1 and white color)
# ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
# cv.imshow('Thresh', thresh)

# contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
# print(f'{len(contours)} contour(s) found!')

# Visualize contours
cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)