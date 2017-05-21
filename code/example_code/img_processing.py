import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])

    lower_green = np.array([50,255,255])
    upper_green = np.array([70,255,255])

    lower = np.array([0,0,0])
    upper = np.array([0,0,0])
    for i in range(3):
        lower[0] = min(lower_blue[0], lower_green[0])
        lower[1] = min(lower_blue[1], lower_green[1])
        lower[2] = min(lower_blue[2], lower_green[2])

        upper[0] = max(upper_blue[0], upper_green[0])
        upper[1] = max(upper_blue[1], upper_green[1])
        upper[2] = max(upper_blue[2], upper_green[2])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower, upper)
    #print mask

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()