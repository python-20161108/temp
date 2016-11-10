#!/usr/bin/env python
#coding=utf-8

from multiprocessing import Pool
import time
import ConfigParser
import os
import urllib
import httplib


global timesleep
timesleep = 5

#
# def bijiao():
#     smmodifytime2 = os.stat (r"smconfig.ini").st_mtime
#     if smmodifytime2 ==smmodifytime:
#         continue
#     else:


def serv(arg):
    print time.time()
    global ipaddr, port, servi, url, servstate
    while True:
        try:
            global timesleep
            ret = os.popen('ps -ef|grep %s|grep -v grep' % arg).readlines()
            if len(ret) > 0:
                params = urllib.urlencode(
                    {arg: "1"}
                )
            else:
                params = urllib.urlencode(
                    {arg: "0"}
                )


            headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}


            httpClient = httplib.HTTPConnection(ipaddr, port, timeout=None)
            httpClient.request("POST", url, params, headers)
            print params
            # response = httpClient.getresponse()
            # print "-----------------------------------------------"
            # print params
            # print response.read()
            # print "------------------------------------------------"
            time.sleep(timesleep)
        except Exception:
            time.sleep(5)
            continue
        except KeyboardInterrupt:
            break
        finally:
            if httpClient:
                httpClient.close()


if __name__ == "__main__":
    poolstatus = True
    while poolstatus:
        try:
            poolstatus = False
            cf = ConfigParser.RawConfigParser()
            cf.read("wanghn.ini")
            ipaddr = cf.get("HostAgent", "ipaddr")
            port = cf.get("HostAgent", "port")
            servi = cf.get("HostAgent", "services")
            url = cf.get("HostAgent", "url")
            servstate = cf.get("HostAgent", "servstate")
            result = servi.split(',')
            alist = ['novell' + x for x in result]
            poolnu = len(result)

            pool = Pool(processes=poolnu)   # 设置进程数量为服务数量
            print ("开始")
            for i in alist:
                result = pool.apply_async(serv, (i,))


        except KeyboardInterrupt:
            pool.close()
            pool.join()
            print("关闭")
            if result.successful():
                print 'successful'
            exit(1)

