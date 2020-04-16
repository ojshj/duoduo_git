from cv2 import cv2
img1 = cv2.imread('samle1.jpg')

#getTickCount:在函数执行之前和之后调用，得到用于执行函数的时钟周期的数目
e1 = cv2.getTickCount()
for i in range(5,49,2):
    img1 = cv2.medianBlur(img1,i)
e2 = cv2.getTickCount()

#getTickFrequency:返回每秒的时钟周期数，下列算式用于得到以秒为单位的执行时间
t = (e2 - e1)/cv2.getTickFrequency()
print(t)
