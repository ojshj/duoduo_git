#!/usr/bin/env python3
# -*- coding: utf-8 -*-

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']#list

print('L[0:3] =', L[0:3])#0,1,2位置的人名
print('L[:3] =', L[:3])#同上
print('L[1:3] =', L[1:3])#1,2
print('L[-2:] =', L[-2:])#4,5

R = list(range(100))#字符转化为列表
print('R[:10] =', R[:10])
print('R[-10:] =', R[-10:])
print('R[10:20] =', R[10:20])
print('R[:10:2] =', R[:10:2])#2表示间隔为2
print('R[::5] =', R[::5])#5表示间隔为5
