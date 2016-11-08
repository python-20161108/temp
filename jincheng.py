#!/usr/bin/env Python
#-*- coding: utf-8 -*-

import os, sys, time

service = 'ndsd'


while True:
    starttime = time.time()

    ret = os.popen('ps -C %s -o pid,cmd' %service).readlines()

    if len(ret) == 2:
        print "%s 进程状态正常！" %name
    elif len(ret) == 3:
        print "%s 进程状态变更！" %name
    elif len(ret) ==1:
        print "%s 进程状态异常！" %name

    stoptime = time.time()
    print "%.2fs" %(stoptime-starttime)
    time.sleep(5)
    