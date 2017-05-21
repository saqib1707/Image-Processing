import cv2
import numpy as np 
import math

img = cv2.imread('My Images/github.jpeg',1)
img_copy = img.copy()

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
'''
temp = np.zeros((100, 100), np.float32)
for i in range(100):
	for j in range(100):
		temp[i,j] = img[100+i, 40+j]
'''
temp = img[100:199, 40: 139]

H, W = img.shape
h, w= temp.shape

res = np.zeros((H-h+1, W-w+1), np.float32)   # np.zeros((rows, cols),--)

for i in range(H-h+1):
	for j in range(W-w+1):
		for k in range(h):
			for l in range(w):
				#if (i+k < W and j+l< H):
				res[i,j] += pow((temp[k,l] - img[i+k, j+l]),2)

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

top_left = min_loc
bottom_right = (top_left[0]+w, top_left[1]+h)

cv2.rectangle(img_copy, top_left, bottom_right, (0,255,0), 2)
cv2.imshow('template image', temp)
cv2.imshow('marked image', img_copy)
cv2.waitKey(0)
cv2.destroyAllWindows()

