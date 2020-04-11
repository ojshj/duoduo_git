# -*- coding: utf-8 -*-

import cv2
import numpy as np

press = False #左键按下为真，松开为假
ix,iy = -1,-1   #ix，iy记录鼠标位置

def draw_circle(event,x,y,flags,param): #鼠标回调函数，鼠标移动绘图
    global ix,iy,press #在函数内部对函数外的变量进行操作，就需要在函数内部声明其为global。

    if event == cv2.EVENT_LBUTTONDOWN:  #按下左键
        press = True
        ix,iy = x,y      #鼠标位置设置成当前位置
        cv2.circle(img,(x,y),5,(0,0,255),-1)

    elif event == cv2.EVENT_MOUSEMOVE:  #鼠标移动
        if  press == True:
            cv2.circle(img,(x,y),5,(0,0,255),-1)

    elif event == cv2.EVENT_LBUTTONUP:  #放开左键
        press = False

img = np.zeros((512,512,3), np.uint8)   #（（行数，列数，通道数），八位无符号整型）
cv2.namedWindow('image')           
cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()