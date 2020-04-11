a = "12345678"

#获取子字符串的位置
print(a.find('3'))

#split
a = "1 2 3 4 5 6"
b = a.split(" ")
print(b)

#打印变量的类型
print("type of a is:", type(a))
print("type of b is:", type(b))

#切片
c = "1234567890"
#打印第3-第5个字符
#print(c[3:5])
#print(c[:-1])
print(c[-5:-1])

#字符串拼接
a1 = "1111"
a2 = "22222"
c = a1+a2
print("c is:", c)

