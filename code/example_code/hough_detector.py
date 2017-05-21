import cv2
import numpy as np

img = cv2.imread('My Images/img30.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize = 3)

lines = cv2.HoughLines(edges,1,np.pi/180,300)
for item in lines:
    for rho,theta in item:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))

        cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

img = cv2.resize(img, (400, 400))
cv2.imshow('hough lines', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#cv2.imwrite('houghlines3.jpg',img)
