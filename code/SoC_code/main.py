import os
import sys
import cv2

if len(sys.argv) > 1:
	path = sys.argv[1]
else:
	path = 'imagelist.txt'

file = open(path, 'r')
filenames = [each.rstrip('\r\n') for each in file.readlines()]
#filenames = [cv2.resize(cv2.imread(each),(480, 320)) for each in filenames]
print 'Files to be stitched\n'+str(filenames)

cmd = './cpp-example-stitching'
for imagefile in filenames:
	cmd += ' '+imagefile
os.system(cmd)