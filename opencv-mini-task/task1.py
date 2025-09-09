import cv2 as cv

# Reading Image
img = cv.imread('../Photos/cats.jpg')

# Display Image
cv.imshow('Cats', img)
print(img.shape)

# Resize Image
width=img.shape[1]
height=img.shape[0]

resized_img=cv.resize(img,(width//2,height//2),interpolation=cv.INTER_AREA)
cv.imshow('Resized Image', resized_img)

print(resized_img.shape)

# Crop Image

mid_h,mid_w=height//2,width//2

# Crop quarters
top_left = img[0:mid_h, 0:mid_w]
top_right = img[0:mid_h, mid_w:width]
bottom_left = img[mid_h:height, 0:mid_w]
bottom_right = img[mid_h:height, mid_w:width]

# Display quarters
cv.imshow('top_left',top_left)
cv.imshow('top_right',top_right)
cv.imshow('bottom_left',bottom_left)
cv.imshow('bottom_right',bottom_right)


# Color Spaces

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

# BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Grayscale to Binary
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Binary', thresh)

cv.waitKey(0)