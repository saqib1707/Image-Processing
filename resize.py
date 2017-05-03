import cv2
import numpy as np

img = cv2.imread('My Images/github.jpeg')

res = cv2.resize(img,None,fx=2, fy=1, interpolation = cv2.INTER_CUBIC)

cv2.imshow('resized image', res)
cv2.waitKey(0)
cv2.destroyAllWindows()