#2 字符串反转
#s = "willing to suffer"
#输出反转后的字符串
s = "willing to suffer"
l3=list(s)
l3.reverse()
print(l3)

#尝试不用reverse, 自己写个函数实现反转
def f(s):
    return s[::-1]
print f(willing to suffer)


#???为什么不行
willing to suffer  没有加引号 "willing to suffer"
print(f(s)) 即可  

还有 注意python2的print
print s 是错误的写法 , 是python2的写法
python3的写法是print(s)