# -*- coding: utf-8 -*-
import cv2
import numpy as np

def get_pixel(event,x,y,flags,param):
  #左键点击  
  if event==cv2.EVENT_LBUTTONDOWN:
      #获取该点的gbr值和hsv值，并打印
      print("HSV is", hsv[y, x])
      
img = cv2.imread("sa.png")
img_mask = np.copy(img)

cv2.namedWindow("input", cv2.WINDOW_AUTOSIZE)
cv2.imshow("input", img)

#将图像转换成hsv像素空间
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#调用鼠标回调函数      
cv2.setMouseCallback('input',get_pixel)    

#设置红色部分的阈值
lower_red_1 = np.array([0,43,46])
upper_red_1 = np.array([10,255,255])

lower_red_2 = np.array([156,43,46])
upper_red_2 = np.array([180,255,255])

#使用inRange函数获取图像中红色部分，赋值给mask_red
mask_red_1 = cv2.inRange(hsv,lower_red_1,upper_red_1)
mask_red_2 = cv2.inRange(hsv,lower_red_2,upper_red_2)
mask_red_sum = mask_red_1+mask_red_2

cv2.imshow("test",mask_red_sum)

#给特定像素赋值
color=[128,9,21]
img_mask[mask_red_sum!=0] = color

cv2.imshow("test2",img_mask)

cv2.waitKey(0)
cv2.destroyAllWindows()
