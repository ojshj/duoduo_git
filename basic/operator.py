
#除法
print("-----除法演示-----")
a = 5
b = 2
c1 = a/b  #除法, 可以返回浮点型
c2 = a//b  #除法, 取整, 取整除 - 返回商的整数部分（向下取整）	
c3 = a%b  #取余

print(c1, c2, c3)


print("-----乘法演示-----")
a = 5
b = 2
print(a*b*b)
print(a**b)  #a的b次方, 幂 - 返回x的y次幂	
print(a**3)

a = 10
a*=3  #a*= 3 等价于a=a*3
#a+= a-=  ....
print("a*=3:", a)

print("-----比较运算符, bool-----")
#bool 就是true or false
print(1 == 2)  #判断两者是否相等
print(1 == 1)
#!=  和  <> 表示不等于
#> < >= <=
#逻辑运算符  and not or
print(1 == 2 and 3 == 4)  #与

#成员运算符
l = [1,2,3,4]
print(5 in l) #false
print(4 in l) #true

#逻辑与数的对应关

#运算符优先级
#逻辑运算符最低
#a*b + c or a/3 + 4
#用简化公式, 去掉复杂的优先级判断
#m = a*b + c   
#n =  a/3 + 4
#q = m or n
#用括号改变优先级
#a + b -c ->a + (b - c)
