# import the necessary packages
from panorama import Stitcher
import argparse
import imutils
import cv2

# load the two images and resize them to have a width of 400 pixels
# (for faster processing)
imageA = cv2.imread('My Images/img01.jpg')
imageB = cv2.imread('My Images/img02.jpg')
'''
cv2.imshow('imageA',imageA)
cv2.imshow('imageB', imageB)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
#imageA = imutils.resize(imageA, width=400)
#imageB = imutils.resize(imageB, width=400)

# stitch the images together to create a panorama
stitcher = Stitcher()
(result, vis) = stitcher.stitch([imageA, imageB], showMatches=True)
 
# show the images
cv2.imshow("Image A", imageA)
cv2.imshow("Image B", imageB)
cv2.imshow("Keypoint Matches", vis)
cv2.imshow("Result", result)
cv2.waitKey(0)