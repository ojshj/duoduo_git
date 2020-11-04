#!/usr/bin/env python
# ‐*‐ coding:utf‐8 ‐*‐
"""code_info
@Time : 2020 2020/11/2 10:33
@Author : Oj
@File : RPI.py
"""
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)   # BCM模式
GPIO.setup(18, GPIO.OUT)

p = GPIO.PWM(18,100)    # 创建一个PWM实例，通道18，频率100Hz
p.start(0)  # 设置占空比为0

delay_time = float(input("The delay time is:"))

while True:
    time_start = time.time()    # 计时
    p.ChageDutyCycle(100)   # 更改占空比为100
    time.sleep(delay_time)    # 睡眠delay_time s
    time_end = time.time()
    print("The close time is:",time_end-time_start)

    p.ChageDutyCycle(50)   # 更改占空比为50
    time.sleep(delay_time)

p.stop()
