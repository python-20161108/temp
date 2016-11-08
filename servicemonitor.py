#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "wanghn"
import httplib
import multiprocessing
import time
import os
import ConfigParser
import urllib

# def settings ():
#     cf = ConfigParser.RawConfigParser ()
#     cf.read ("smconfig.ini")
#     url = cf.get ("HostAgent", "services")
#     servstate = cf.get("HostAgent", "disknu")
#     result = url.split (',')
#     return result

def serv(arg):
    # global httpClient
    try:
        while True:
            try:
                # smmodifytime2 = os.stat (r"smconfig.ini").st_mtime
                # if smmodifytime2 ==smmodifytime:
                #     continue
                # else:
                ret = os.popen ('ps -ef|grep %s|grep -v grep' %arg).readlines()
                if len (ret) > 0:
                    ser = "%s1" %arg
                    params = urllib.urlencode(
                        {servstate: ser
                         }
                    )
                # print "%s 进程状态正常！" % arg, time.strftime ('%Y-%m-%d %H:%M:%S', time.localtime (time.time ()))
                # print '======================================'
                else:
                    # return '%s:0' % arg
                    ser = "%s0" %arg
                    # ser = '%s\\:0' % arg
                    params = urllib.urlencode(
                        {servstate: ser
                         }
                    )
                # print "%s 进程状态异常！" % arg, time.strftime ('%Y-%m-%d %H:%M:%S', time.localtime (time.time ()))
                # print '======================================'
                time.sleep (3)
                headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
                middletime = time.time ()
                # httpClient = httplib.HTTPConnection ("192.168.0.138", 8080, timeout=30)
                # httpClient.request ("POST", "/edCenter/module/welcome/getDataTestAction", params, headers)
                httpClient = httplib.HTTPConnection( ipaddr, port, timeout=None)
                httpClient.request("POST", url, params, headers)
                response = httpClient.getresponse ()
                print "-----------------------------------------------"
                print params
                print response.read ()
                print "------------------------------------------------"
                stoptime = time.time ()
            except Exception,e:
                #  print "5秒后重试......"
                time.sleep(5)
                continue
    except KeyboardInterrupt:
        exit (1)
    except Exception, e:
        exit (1)
    finally:
        if httpClient:
            httpClient.close()
try:
    starttime = time.time ()
    result = []
    if __name__ == '__main__':
        # service = settings ()
        cf = ConfigParser.RawConfigParser ()
        cf.read ("/root/python/wanghn.ini")
        ipaddr = cf.get ("HostAgent", "ipaddr")
        port = cf.get ("HostAgent", "port")
        servi = cf.get ("HostAgent", "services")
        url = cf.get ("HostAgent", "url")
        servstate = cf.get ("HostAgent", "servstate")
        result = servi.split (',')
        alist = ['novell' + x for x in result]
        servlen = len (result)
        for i in xrange (servlen):
            alist[i] = multiprocessing.Process (target=serv, args=(result[i],))
            alist[i].start ()
except Exception, e:
    print e
except KeyboardInterrupt:
    exit ()
