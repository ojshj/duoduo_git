#6 字符串到字典
#将字符串："k:1|k1:2|k2:3|k3:4"，处理成 python 字典：{'k':'1', 'k1':'2', 'k2':'3','k3':'4' }

dict={}
dict[k]=1
dict[k1]=2
dict[k2]=3
dict[k3]=4
print(dict)


#不是这样, 应该是
#s = "k:1|k1:2|k2:3|k3:4"
#写个函数, 输入s ,输出这个字典

s = "k:1|k1:2|k2:3|k3:4"
dict1=eval(s)
print(dict1)

#根本跑不起来 糊弄自己呢 
#提示  先风格为一个list  ['k:1', 'k:2' ...]
#再对list每个元素风格为 [['k', '1'], ...]
#再转换为字典
 

s = "k:1|k1:2|k2:3|k3:4"
l1 = s.split("|")
print("l1 is:", l1)

l2 = []
for a in l1:
    l2.append(a.split(":"))
print("l2 is:", l2)

d1 = {}
for a in l2:
    d1[a[0]] = a[1] 