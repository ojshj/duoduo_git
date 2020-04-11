# -*- coding: utf-8 -*-
import cv2
import numpy as np

#回调函数。pass：do nothing 
def nothing(x):
    pass

img = np.zeros((300,512,3), np.uint8)
cv2.namedWindow('image')

#createTrackbar（）函数用于创建轨迹条
#调色轨迹条       #名称，窗口，轨迹条位置，最大值，引用回调函数
cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)

#开关
switch = '0 : OFF \n1 : ON'
#用于决定开启或关闭调色状态
cv2.createTrackbar(switch, 'image',0,1,nothing)

#展示图像
while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    #getTrackbarPos（）函数用来获取当前轨迹条的位置
    r = cv2.getTrackbarPos('R','image')
    g = cv2.getTrackbarPos('G','image')
    b = cv2.getTrackbarPos('B','image')
    s = cv2.getTrackbarPos(switch,'image')

    if s == 0:    #非调色状态
        img[:] = 0
    else:         #调色状态
        img[:] = [b,g,r]

cv2.destroyAllWindows()