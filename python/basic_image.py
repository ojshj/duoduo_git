# -*- coding: utf-8 -*-
import cv2
img=cv2.imread('sample.jpg',0)
cv2.imshow('image',img)       #open a window

cv2.waitKey(0)                #a keyboard binding function
cv2.destroyAllWindows()       #distroy windows
cv2.imwrite('sample.png',0)   #save an image

from matplotlib import pyplot as plt #matplotlib : a plotting library
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.show()
