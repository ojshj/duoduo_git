# -*- coding: utf-8 -*-
import cv2
import numpy as np

def draw_circle(event,x,y,flags,param):        #鼠标回调函数
    if event==cv2.EVENT_LBUTTONDBLCLK:         #双击左键
        cv2.circle(img,(x,y),100,(255,0,0),-1) #画圆

               #三维矩阵    无符号8bit整数
img = np.zeros((512,512,3), np.uint8) 
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)      #调用鼠标回调函数
 
while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(20) & 0xFF == 27:           #&位运算符，键盘键入取尾两个字节
        break

cv2.destroyAllWindows()