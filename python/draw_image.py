# -*- coding: utf-8 -*-
import numpy as np
import cv2

#创建一个图像
img = np.zeros((512,512,3), np.uint8)

#划线    图像 起点  终点      颜色      厚度
cv2.line(img,(0,0),(511,511),(255,0,0),1)

#矩形             
cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)

#圆             圆心     半径  颜色     厚度（-1表示实心
cv2.circle(img,(447,63), 63, (0,0,255), -1)

#椭圆            中心      长轴短轴 旋转角度 颜色
cv2.ellipse(img,(256,256),(100,50),0,0,180,(255,0,0),-1)

#多边形         各个顶点的坐标                    32位整数类型
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(0,255,255))#true表示闭合

#定义字体
font = cv2.FONT_HERSHEY_SIMPLEX
#文字       图像 文字内容 坐标      字体 大小  颜色      字体厚度
cv2.putText(img,'00202',(10,500), font, 4,(255,255,255),2)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()