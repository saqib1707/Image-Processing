import cv2
import numpy as np
import math

img = cv2.imread('My Images/opencvlogo.png')

rows, cols, ch = img.shape
th = (30*math.pi)/180
#mat = np.float32([[math.cos(th),-1*math.sin(th),150],[math.sin(th),math.cos(th), -50],
#					[0, 0, 1]])
mat = np.float32([[1,0,0.001],[0, 1, 0],[-200,-300,1]])

#out = cv2.warpAffine(img, mat, (rows, cols))
out = cv2.warpPerspective(img, mat, (cols, rows))
cv2.imshow('input', img)
cv2.imshow('out', out)
cv2.waitKey(0)
cv2.destroyAllWindows()