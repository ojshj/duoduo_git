from cv2 import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('sample1.jpg')
rows,cols,ch = img.shape

#resize：缩放
res = cv2.resize(img,None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC)
#res = cv2.resize(img,(2*cols, 2*rows), interpolation = cv2.INTER_CUBIC)

'''
#平移
#np.float32：类型是np.float32的Numpy数组
M =  np.float32([[1,0,100],[0,1,50]])
#warpAffine：对图像进行矩阵变换
# （图像，转换矩阵，（输出图像列数，行数））                
dst = cv2.warpAffine(img,M,(cols,rows))

#旋转
#getRotationMatrix2D：创建一个旋转矩阵
# （旋转中心，角度，缩放因子）
M = cv2.getRotationMatrix2D((cols/2,rows/2), 90, 1)
dst = cv2.warpAffine(img, M, (cols, rows))

#仿射变换
             #变换的中间矩阵
pts1 = np.float32([[50,50],[200,50],[50,200]])  #变换前的三个点的位置
pts2 = np.float32([[10,100],[200,50],[100,250]])#变换后这三点的位置

#getAffineTransform：由三个点的变换得出整张图变换的矩阵
M = cv2.getAffineTransform(pts1, pts2)
dst = cv2.warpAffine(img,M,(cols, rows))

plt.plot(x, y) #绘制x-y直角坐标图
#subplot(121)一行二列个图像，第二个1表示该图在第一个位置 
plt.subplot(121), plt.imshow(img), plt.title('Input')
plt.subplot(122), plt.imshow(dst), plt.title('Output')
plt.show()
'''

#透视变换（投影）
pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])#变换前四个点的位置
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])    #变换后四个点的位置

#getPerspectiveTransform：有四个点变换的得出变换矩阵
M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(img,M,(300,300))

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()

cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()