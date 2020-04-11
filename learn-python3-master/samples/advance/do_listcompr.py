#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print([x * x for x in range(1, 11)])#平方
print([x * x for x in range(1, 11) if x % 2 == 0])#2的倍数平方
print([m + n for m in 'ABC' for n in 'XYZ'])#abc中任意字符加xyz中任意字符

d = {'x': 'A', 'y': 'B', 'z': 'C' }#字典d
print([k + '=' + v for k, v in d.items()])输出为k=v,k,v为d中任意字符

L = ['Hello', 'World', 'IBM', 'Apple']#list
print([s.lower() for s in L])#l中的大写字符转化为小写
