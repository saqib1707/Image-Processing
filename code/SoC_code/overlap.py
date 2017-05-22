import cv2
import numpy as np
import sys

if len(sys.argv)>=2:
	path_1 = sys.argv[1]
else:
	path_1 = '../images/2Hill.JPG'
if len(sys.argv)>=3:
	path_2 = sys.argv[2]
else:
	path_2 = '../images/3Hill.JPG'

img1 = cv2.imread(path_1)
img2 = cv2.imread(path_2)

r1, c1, ch1 = img1.shape
r2, c2, ch2 = img2.shape

#print (r1 == r2)
#print (c1 == c2)
count_match = 0
col1 = col2 = 0
#flag = False
while col1 < c1:
	error_count = 0
	for row in range(r1):
		p1 = pow((float(img1[row,col1][0]-img2[row,col2][0])/255),2)
		p2 = pow((float(img1[row,col1][1]-img2[row,col2][1])/255),2)
		p3 = pow((float(img1[row,col1][2]-img2[row,col2][2])/255),2)
		print (p1+p2+p3)
		if (p1 + p2 + p3 >= 1.5):
			error_count+=1

	if error_count <= r1/10:
		col2 += 1
		count_match += 1
	col1 += 1
	#print error_count

'''
while col1 < c1:
    while col2 < c2:
        if (img1[:, col1] == img2[:, col2]):
            count_match+=1
            col2 += 1
            break
        col2 = (col2+1)%(c2+1)
    col1 = col1+1
    if col2 == c2:
        col2 = 0
'''
print 'No of columns matched:'+str(count_match)
intersection = r1*count_match
union = r1*c1 + r2*c2 - intersection

per_overlap = (float(intersection)/union)*100

print 'Percentage overlap between images:'+str(per_overlap)