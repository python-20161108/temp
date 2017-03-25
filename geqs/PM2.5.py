#!/bin/env python
# -*- coding: utf-8 -*-
# 计算空气质量情况

PM = input("今天PM2.5的数值是多少?请输入:")
if PM > 75:
    print("今天的天气很差！")
if PM < 35:
    print("今天的天气很好!")
