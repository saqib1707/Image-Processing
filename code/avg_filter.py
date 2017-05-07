import cv2
import numpy as np
from matplotlib import pyplot as plt
from convolution import convolve

img = cv2.imread('My Images/github.jpeg')
#blur = cv2.blur(img,(5,5))
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

kernel = np.ones((5,5), np.float32)/25
dst = convolve(img, kernel)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()