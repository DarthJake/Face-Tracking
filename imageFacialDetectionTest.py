import numbers as np
import cv2
import matplotlib.pyplot as plt

def detect(image):
    # Need this
    haar_cascade_face = cv2.CascadeClassifier('./build/opencv/sources/data/haarcascades/haarcascade_frontalface_default.xml')

    # Dont want to change original. making copy
    image_copy = image.copy()

    # Convert to grayscale becasue gray input is expected
    image_gray = cv2.cvtColor(image_copy, cv2.COLOR_BGR2GRAY)

    # Apply Haar cascade to detect faces
    faces = haar_cascade_face.detectMultiScale(image_gray, scaleFactor = 1.1, minNeighbors = 5)

    # Loop through faces and apply rectangle
    for (x, y, w, h) in faces:
        cv2.rectangle(image_copy, (x, y), (x+w, y+h), (0, 255, 0), 8)
    
    return image_copy

def convertToRGB(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


new_image = detect(cv2.imread('./test2.png'))

cv2.imshow('detection', new_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# plt.imshow(convertToRGB(new_image))
# plt.show()