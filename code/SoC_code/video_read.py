import numpy as np
import cv2

cap = cv2.VideoCapture('ImageStitching.wmv')
i =0
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret is False:
    	break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if i%10 == 0:
    	cv2.imwrite('img0'+str(i)+'.jpg', gray)
    i += 1
    cv2.imshow('frame',gray)
    cv2.waitKey(20)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()