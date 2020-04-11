a= [1,2,3,4,5]
b = [i*2 for i in a]  #这就是列表推导
print(b)

#字典推导
d = {i:1 for i in a}
print(d)

l = [1,2,3,4,5,6]
len_l = len(l) #获取list长度
for i in range(len_l):  #遍历list下标
    l[i] *= 10  #根据下标取元素, X10
print(l)