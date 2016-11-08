#!/usr/bin/env python
# coding=utf8

import httplib, urllib
import time
import random
import sys

httpClient = None

try:
    while True:
        try:
            msg = str(random.randint(1, 100))  # 产生随机数

            timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

            params = urllib.urlencode(
                {'time': timenow,
                 'data': msg
                 })

            headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}

            httpClient = httplib.HTTPConnection("192.168.0.138", 8080, timeout=30)
            http_Client_request = httpClient.request("POST", "/edCenter/api.jsp", params, headers)

            response = httpClient.getresponse() # 获取服务器返回信息
            print response.status   # 获取访问状态
            print response.reason
            print response.read()   # 获取访问数据
            print response.getheaders()  # 获取头信息

        except KeyboardInterrupt:   # 内循环如果按下Crlt + C 跳出while循环
            break   # 跳出本循环体

        except:
            print("%s: http服务器连接异常，5秒后自动重试！！！" %(time.ctime()))
            time.sleep(5)
            continue    # 结束本次循环

        time.sleep(3)   # 等待3秒

except KeyboardInterrupt:   # Ctrl + C 结束异常
    sys.exit(0) # 系统执行（0）正常退出，（1）异常退出

finally:
    print("--------------------------------------------------")
    if httpClient:
        print("http连接正在关闭！")
        httpClient.close()
        print("http连接关闭完成！")
    else:
        print("http连接关闭完成！")
