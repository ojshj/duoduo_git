#数据类型
#整形, 就是整数, 比如-1, 1, 0, 整形= int
i = 1
print("type of i is:", type(i))

#浮点, 小数, 比如0.1, -0.1, 科学记数法表示的小数, 比如1e-4, 浮点 = float
f = 0.1123
print("type of f is:", type(f))

#字符串
s = "abcd"
print("type of s is:", type(s))

#元组 = tuple
t1 = (1 ,2, 3, 4, 5)
print("type of l1 is:", type(t1))

#队列 = list, 用中括号括起来的一组数据
l1 = [1 ,2, 3, 4, 5]
l2 = ["1", "2", "3", "4", "5"]
l3 = [1 ,2, 3, "4"]
print("type of l1 is:", type(l1))

#tuple 和list的差别, list的元素可以改变, tuple的元素不可以改变
l1[0] = 2
print(l1)

#下面两行会报错, 因为tuple元素不可改变
#t1[0] = 2
#print(t1)

#字典 dictionary {key:value}
d = {"duoduo":18, "binfeng":31, "tingxue":2}
print(d)
print(d.keys())
print("duoduo de age is:", d["duoduo"])

