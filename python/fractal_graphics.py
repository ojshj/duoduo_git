#!/usr/bin/env python
# ‐*‐ coding:utf‐8 ‐*‐
"""code_info
@Time : 2020 2020/11/2 8:08
@Author : Oj
@File : fractal_graphics.py
"""
import turtle


# 一条直线
def a_line(length,level):
    if level == 0:
        turtle.fd(length)
    else:
        # 依次采取0,60,-120,60作为角度绘制，完成分形图的一条线
        for i in [0,60,-120,60]:
            turtle.left(i)
            a_line(length/3,level-1)


def c():
    length = 500    # 移动距离
    level = 5   # 五层作为一个整体迭代
    angle = 120    # 角度
    turtle.hideturtle()
    turtle.speed(10)

    # 从（-300，200）开始绘制
    turtle.penup()
    turtle.goto(-300,200)
    turtle.pendown()

    a_line(length,level)
    turtle.right(angle)    # 顺时针移动120°
    a_line(length, level)
    turtle.right(angle)
    a_line(length, level)
    turtle.right(angle)

    turtle.done()


c()
