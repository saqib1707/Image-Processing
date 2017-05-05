import cv2

stitcher = cv2.createStitcher(False)
img = cv2.imread("My Images/github.jpeg")

img1 = img[0:200, 0:200]

img2 = img[150:300, 150:300]

result = stitcher.stitch((img1, img2))

cv2.imwrite("My Images/stiched.jpeg", result[1])