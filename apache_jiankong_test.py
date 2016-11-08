#!/usr/bin/env Python
#-*- coding: utf-8 -*-

import os
import time

while True:
    try:
        ret = os.popen('ps -C apache -o pid,cmd').readlines()
        if len(ret) < 2:
            print "apache 进程异常退出， 5 秒后重新启动!!!"
            time.sleep(3)
            os.system("service apache2 restart")
    except KeyboardInterrupt:
        exit(0)
    finally:
        time.sleep(5)
