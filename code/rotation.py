import cv2
import numpy as np 
img = cv2.imread('My Images/github.jpeg',0)
rows,cols = img.shape
 
M = cv2.getRotationMatrix2D((cols/2,rows/2),23,1)
print M
dst = cv2.warpAffine(img,M,(cols,rows))
cv2.imshow('original image', img)
cv2.imshow('rotated image', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()