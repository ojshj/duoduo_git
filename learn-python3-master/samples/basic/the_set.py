#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#set为内置函数,set() 函数创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等

s1 = set([1, 1, 2, 2, 3, 3])
print(s1)
s2 = set([2, 3, 4])
print(s1 & s2)
print(s1 | s2)
