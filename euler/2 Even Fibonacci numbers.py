a=1
b=2
l=[a, b]

#生成斐波那契数列
while True:
    c=a+b
    a=b
    b=c

    if c >= 4000000:
        break
    else:
        #将c添加到l
        l.append(c)

print(l)
    
#累加偶数
sum = 0
for number in l:
    if number % 2 == 0:
        sum += number
        print(number)


print(sum)