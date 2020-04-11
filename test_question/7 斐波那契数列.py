#7 斐波那契数列
#输出<1000000的斐波那契数列

a=1
b=2
l=[a, b]
while True:
    c=a+b
    a=b
    b=c
    if c >= 1000000:
        break
    else:
        l.append(c)

print(l)
