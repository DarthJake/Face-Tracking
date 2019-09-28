import numpy as np
import cv2


def detect(image):
    # Need this
    haar_cascade_face = cv2.CascadeClassifier(
        './../build/opencv/sources/data/haarcascades/haarcascade_frontalface_default.xml')
    
    # Dont want to change original. making copy
    image_copy = image.copy()

    # Convert to grayscale becasue gray input is expected
    image_gray = cv2.cvtColor(image_copy, cv2.COLOR_BGR2GRAY)

    # Apply Haar cascade to detect faces
    faces = haar_cascade_face.detectMultiScale(
        image_gray, scaleFactor=1.1, minNeighbors=5)

    # Loop through faces and apply rectangle
    for (x, y, w, h) in faces:
        cv2.rectangle(image_copy, (x, y), (x+w, y+h), (0, 255, 0), 8)

    return image_copy


camera = cv2.VideoCapture(0)

while(True):
    ret, frame = camera.read()
    render = detect(frame)

    print(type(frame))
    print(type(render))

    cv2.imshow('render', render)

    if (cv2.waitKey(20) & 0xFF == ord('q')):
        break

camera.release()
cv2.destroyAllWindows()
