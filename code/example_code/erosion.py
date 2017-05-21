import cv2
import numpy as np


img = cv2.imread('My Images/github.jpeg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret,img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
kernel = np.ones((5,5),np.uint8)

erode = cv2.erode(img,kernel, iterations=1)
dilation = cv2.dilate(erode, kernel, iterations =1)


cv2.imshow('original image',img)
cv2.imshow('eroded image',erode)
cv2.imshow('dilation image',dilation)
cv2.waitKey(0)
cv2.destroyAllWindows()