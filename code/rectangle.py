import cv2
import numpy as np 
from matplotlib import pyplot as plt 

img = cv2.imread('My Images/github.jpeg',1)
h, w , t= img.shape
#$img = np.zeros((512,512,3), np.uint8)
#cv2.line(img,(0,0),(511,400),(255,0,0),5)
#cv2.rectangle(img,(384,0),(510,400),(0,255,0),10)
cv2.circle(img,(w/2,h/2), 60, (0,0,255), 1)
cv2.imshow('image', img)
cv2.waitKey(0)
