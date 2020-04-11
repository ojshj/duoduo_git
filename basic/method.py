#method = function  函数, 实现某种特定操作的的一套代码的封装

print("第一个函数测试:")
#定义一个函数
def addOne(p):
   return p + 1

#调用函数
print(addOne(1))
print(addOne(100))


print("第二个函数测试:")
#定义一个函数
def add(a, b):
   return a+b

#调用函数
print(add(1, 3))

print("第二个函数测试:")
#定义一个函数
def print_people_into(name):
    if name == "duoduo":
       print("name is:", name)
       print("age is:", 18)
       print("gender is:", "female")
    elif name == "binfeng":
        print("i dont konw")

#调用函数
print_people_into("binfeng")


#f(x) = sin(a) + cos(b)
import math #导入数学库, math是包名称
def f(a , b):
    return math.sin(a) + math.cos(b)
print(f(3.14, 6.28))