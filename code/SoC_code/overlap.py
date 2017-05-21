import cv2
import numpy as np

img1 = cv2.imread(' ')
img2 = cv2.imread(' ')

r1, c1, ch1 = img1.shape
r2, c2, ch2 = img2.shape

count_match = 0
col1 = col2 = 0
while col1 < c1:
    while col2 < c2:
        if (img1[:, col1] = img2[:, col2]):
            count_match+=1
            col2 += 1
            break
        col2 = (col2+1)%(c2+1)
    col1 = col1+1
    if col2 == c2:
        col2 = 0

print 'No of columns matched:'+str(count_match)
intersection = r1*count_match
union = r1*c1 + r2*c2 - intersection

per_overlap = (intersection/union)*100

print 'Percentage overlap between images:'+str(per_overlap)


        
