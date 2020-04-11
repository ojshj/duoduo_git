#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#遍历0到4的数字,平方输入s,输出s
s = (x * x for x in range(5))
print(s)
for x in s:#遍历s中的数值,输出
    print(x)

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:#当n比print值小,循环
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

f = fib(10)#10为上文所属max
print('fib(10):', f)
for x in f:
    print(x)

# call generator manually:
g = fib(5)
while 1:#非0就是true,即while ture
    try:
        x = next(g)#下一个
        print('g:', x)
    except StopIteration as e:#换元
        print('Generator return value:', e.value)
        break

