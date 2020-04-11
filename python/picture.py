# -*- coding: utf-8 -*-

import cv2 as cv

#读取图像
src=cv.imread('example.png')

#namedWindow函数，用于创建一个窗口       
cv.namedWindow('input_image')

#指定窗口显示图像，‘input_image'：窗口名；src：要显示的图像
cv.imshow('input_image', src)

#翻转
h_flip = cv.flip(src, 1)#水平翻转
v_flip = cv.flip(src, 0)#垂直翻转
hv_flip = cv.flip(src, -1)#水平垂直翻转

#保存图像 
cv.imwrite("v_flip.jpg", v_flip)
cv.imwrite("h_flip.jpg", h_flip)
cv.imwrite("hv_flip.jpg", hv_flip)

#绑定键盘，0指永远
cv.waitKey(0)

#删除所有窗口，可用窗口名做参数表示删除指定窗口
cv.destroyAllWindows()  

















