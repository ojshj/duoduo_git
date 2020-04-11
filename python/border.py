# -*- coding: utf-8 -*-

import cv2
from matplotlib import pyplot as plt

BLUE = [255,0,0]

img1 = cv2.imread('sample.jpg')

replicate = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REPLICATE)

reflect = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_WRAP)
constant= cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_CONSTANT,value=BLUE)


plt.subplot(231)         #使用plt.subplot来创建小图.
                         #plt.subplot(231)表示将整个图像窗口分为2行3列, 当前位置为1.
plt.imshow(img1,'gray')
plt.title('ORIGINAL')    #展示原图

plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')

plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')


plt.show()