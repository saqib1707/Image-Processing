import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('My Images/github.jpeg',0)
img2 = img.copy()
'''
template = np.zeros((100, 100), np.uint8)
for i in range(100):
	for j in range(100):
		template[i,j] = img[100+i, 40+j]
'''
template = img[100:199, 40: 139]

w, h = template.shape[::-1]
method = eval('cv2.TM_SQDIFF')
res = cv2.matchTemplate(img,template,method)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
top_left = min_loc
bottom_right = (top_left[0] + w, top_left[1] + h)

cv2.rectangle(img,top_left, bottom_right, 255, 2)

cv2.imshow('original image', img)
cv2.imshow('marked image', res)
cv2.waitKey(0)
cv2.destroyAllWindows()