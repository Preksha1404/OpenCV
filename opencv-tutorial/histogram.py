import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img=cv.imread('../Photos/cats.jpg')
cv.imshow('Cats',img)

# gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('GrayScale Image',gray)

# Grayscale histogram
# gray_hist = cv.calcHist([gray], [0], None, [256], [0,256] )
# plt.figure()
# plt.title('Grayscale Histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()

# Masked Grayscale histogram
# blank=np.zeros(img.shape[:2],dtype='uint8')

# circle=cv.circle(blank.copy(),(img.shape[1]//2,img.shape[0]//2),100,255,-1)

# mask=cv.bitwise_and(gray,gray,mask=circle)
# cv.imshow('Mask',mask)

# gray_hist = cv.calcHist([gray], [0], mask, [256], [0,256] )
# plt.figure()
# plt.title('Grayscale Histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()

# Color Image histogram
plt.figure()
plt.title('Colour Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
colors = ('b', 'g', 'r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])
plt.show()

cv.waitKey(0)