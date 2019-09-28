import cv2
import numpy as np

capture = cv2.VideoCapture(0)

while(True):
    ret, frame = capture.read()

    grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display Results
    cv2.imshow('frame', frame)
    cv2.imshow('gray', grayscale)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
    
capture.release()
cv2.destroyAllWindows()