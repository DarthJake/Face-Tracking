import numpy as np
import cv2

img = cv2.imread('./mandrill.png', cv2.IMREAD_GRAYSCALE)

while True:
    cv2.imshow('mandrill', img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.imwrite('gray_mandrill.png', img)
cv2.destroyAllWindows()
