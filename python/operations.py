# -*- coding: utf-8 -*-
from cv2 import cv2

img1 = cv2.imread('sample1.jpg')
img2 = cv2.imread('sample2.png')

'''
#需要两图深度及类型一致
#(图像1，权重，图像2，权重，添加到结果的标量，默认为0)
dst = cv2.addWeighted(img1,0.7,img2,0.3,0)
'''

#将图二的行数列数通道数返回给rows,cols,channels
rows,cols,channels = img2.shape

#将图一的从第零行到第rows行，第零列到第cols列包围的区域设置为感兴趣区域
roi = img1[0:rows, 0:cols ]

#将图像二转为灰色图像
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

#threshold：灰度图像二值化函数（图像，阈值，最大值，阈值类型）
#返回值ret为设置的阈值，mask为处理完的图像
ret, mask = cv2.threshold(img2gray, 175, 255, cv2.THRESH_BINARY)

#按位not运算
mask_inv = cv2.bitwise_not(mask)

cv2.imshow('mask',mask)
cv2.imshow('mask_inv',mask_inv)

#按位加；前面两幅图AND后再与mask做AND，使原图中掩码为1的像素变为1（全黑）
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)

#按位加
img2_fg = cv2.bitwise_and(img2,img2,mask = mask)

cv2.imshow('bg',img1_bg)
cv2.imshow('fg',img2_fg)

#把拼合的图像赋给图一
dst = cv2.add(img1_bg,img2_fg)
img1[0:rows, 0:cols ] = dst

cv2.imshow('res',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()