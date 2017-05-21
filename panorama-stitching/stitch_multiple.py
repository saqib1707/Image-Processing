# USAGE
# python stitch.py --first images/bryce_left_01.png --second images/bryce_right_01.png 

# import the necessary packages
from pyimagesearch.panorama import Stitcher
import argparse
#import imutils
import cv2

# construct the argument parse and parse the arguments
'''
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--first", required=True,
	help="path to the first image")
ap.add_argument("-s", "--second", required=True,
	help="path to the second image")
args = vars(ap.parse_args())
'''

if __name__ == '__main__':
	try:
		args = sys.argv[1]
	except:
		args = "txtlists/files1.txt"
	finally:
		print "Parameters : ", args

	fp = open(args, 'r')
	filenames = [each.rstrip('\r\n') for each in  fp.readlines()]
	print filenames
	#images = [cv2.resize(cv2.imread(each),(480, 320)) for each in filenames]
	images = [cv2.resize(cv2.imread(each), (480,320)) for each in filenames]
	count = len(images)

	#left_list, right_list, center_im = [], [],None

	# load the two images and resize them to have a width of 400 pixels
	# (for faster processing)
	#imageA = cv2.imread(args["first"])
	#imageB = cv2.imread(args["second"])
	#imageA = imutils.resize(imageA, width=400)
	#imageB = imutils.resize(imageB, width=400)
	imageA = images[0]
	stitcher = Stitcher()
	for imageB in images[1:]:
		# stitch the images together to create a panorama
		(result, vis) = stitcher.stitch([imageA, imageB], showMatches=True)
		imageA = result

	# show the images
	cv2.imshow("Image A", imageA)
	cv2.imshow("Image B", imageB)
	cv2.imshow("Keypoint Matches", vis)
	cv2.imshow("Result", result)
	cv2.waitKey(0)