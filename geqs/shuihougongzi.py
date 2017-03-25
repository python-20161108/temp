#!/bin/env python
# -*- coding: utf-8 -*-
# 计算税后工资


def is_number(s):  # 自定义函数判断是否为数字！
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


def nashui(J):  # 计算纳税后工资！
    # G = '%.2f' %(J - 3500)
    G = J - 3500
 
    # 计算超过3500部分纳税金额!
    if G > 0 and G <= 1500:   
            print(6)
            print("你工资税部分金额是%s,纳税金额%s！" %(G, G*0.03))
    
    if G > 1500 and G <= 4500:
            print(5)
            print("你工资税部分金额是%s,纳税金额%s！" %(G,G*0.1-105))
            # return G*0.1-105

    if G > 4500 and G <= 9000:
            print(4)
            print("你工资税部分金额是%s,纳税金额%s！" %(G,G*0.2-555))

    if G > 9000 and G <= 35000:
            print(3)
            print("你工资税部分金额是%s,纳税金额%s！" %(G,G*0.25-1005))

    if G > 35000 and G <= 55000:
            print(2)
            print("你工资税部分金额是%s,纳税金额%s！" %(G,G*0.35-5505))
        
    if G > 55000 and G <= 80000:
            print(1)
            print("你工资税部分金额是%s,纳税金额%s！" %(G,G*0.35-5505))
    
    if G > 80000:
            print("暂时不支持计算超过税点后80000，谢谢！")


def inputs():
    I = input("你的税前工资是多少？\n请输入:")
    if len(I) != 0 and is_number(I) == True:
        J = int(I)
        if J <= 3500:
            print("\n悲惨倒霉的朋友，工资还不够交税的！\n如果我挣钱这么少我都不好意思用这个程序算！\n退下把！")
            
        else:
            nashui(J)
    else:
        print("你输入的不合法,请重新输入！")
        inputs()

inputs()
