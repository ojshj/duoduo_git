# -*- coding: utf-8 -*-
import cv2
import numpy as np

#参数为0，打开摄像头；参数为路径，打开视频
cap = cv2.VideoCapture(0)

while(1):
    #读取每帧吗，ret,frame是cap.read()的两个返回值
    #ret是布尔值，如果读取帧是正确的则返回True，如果文件读取到结尾，它的返回值就为False
    #frame就是每一帧的图像，是个三维矩阵
    ret, frame = cap.read()

    #由BRG转换为HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #定义HSV中蓝色的范围
    lower_blue = np.array([110,50,50])   #下界
    upper_blue = np.array([130,255,255]) #上界

    #设置图像的阈值仅获取蓝色（图像，读取颜色下界，读取颜色上界）
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    #按位与操作，mask掩模：白色区域为对处理图像像素的保留，黑色剔除
    res = cv2.bitwise_and(frame,frame, mask= mask)

    #显示图像
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()