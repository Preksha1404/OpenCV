import cv2 as cv

# Detect faces from image
# img=cv.imread('../Photos/lady.jpg')
# cv.imshow('Person',img)

# img=cv.imread('../Photos/group 1.jpg')
# cv.imshow('Group of people',img)

# gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('Gray Person',gray)

# haar_cascade=cv.CascadeClassifier('../haar_face.xml')

# faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)

# print(f'Number of faces found = {len(faces_rect)}')

# for (x,y,w,h) in faces_rect:
#     cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

# cv.imshow('Detected Faces', img)

# cv.waitKey(0)


# Detect face from video
capture=cv.VideoCapture('../Videos/person.mp4')

haar_cascade=cv.CascadeClassifier('../haar_face.xml')

while True:
    isTrue, frame = capture.read()

    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)

    if isTrue:    
        # cv.imshow('Video', frame)
        display_frame = cv.resize(frame, (800, 600))
        cv.imshow('Video', display_frame)
        faces_rect = haar_cascade.detectMultiScale(display_frame, scaleFactor=1.1, minNeighbors=1)

        '''
        detectMultiScale --> detect faces by scaling factor=1.1 and minNeighbors=5
        scaling factor-> detect face by zooming by scaling factor value each time until it detect face
        minNeighbors->safe checking (check for that many times for detected faces)
        '''

        for (x,y,w,h) in faces_rect:
            cv.rectangle(display_frame, (x,y), (x+w,y+h), (0,255,0), thickness=2)
        
        '''
        x,y,w,h --> 
        x->how far from left
        y->how far from top
        w->width of face
        h->height of face
        x,y-->top-left corner
        x+w,y+h-->bottom-right corner
        '''
        cv.imshow('Detected Faces in Video', display_frame)

        if cv.waitKey(20) & 0xFF==ord('d'):
            break            
    else:
        break

capture.release()
print(f'Number of faces found = {len(faces_rect)}')