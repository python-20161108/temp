#!/bin/env python

import time


def getcpu():
    with open('/proc/stat') as f:
        cpu_1 = f.readline().split()
        sys_idel_1 = int(cpu_1[4])
        total_1 = int(cpu_1[1]) + int(cpu_1[2]) + int(cpu_1[3]) + int(cpu_1[4]) + int(cpu_1[5]) + int(cpu_1[6]) + int(cpu_1[7])
        time.sleep(1)
    with open('/proc/stat') as f:
        cpu_2 = f.readline().split()
        sys_idel_2 = int(cpu_2[4])
        total_2 = int(cpu_2[1]) + int(cpu_2[2]) + int(cpu_2[3]) + int(cpu_2[4]) + int(cpu_2[5]) + int(cpu_2[6]) + int(cpu_2[7])
    print sys_idel_1, sys_idel_2
    print total_1, total_2
    # disp_sys_rate = (100 - (sys_idel_2 - sys_idel_1) / (total_2 - total_1) * 100)/1
    # print disp_sys_rate
    # return disp_sys_rate


def getmem():
    with open('/proc/meminfo') as f:
        total = int(f.readline().split()[1])
        free = int(f.readline().split()[1])
        buffers = int(f.readline().split()[1])
        cache = int(f.readline().split()[1])
    mem_use = (total - free - buffers - cache)/1024
    return mem_use


def info():
    while True:
        timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        print timenow
        print getcpu()
        # print getmem()
        time.sleep(3)


info()
# getcpu()
