#!/usr/bin/env python
#coding=utf8
 
import httplib, urllib
import time
import os
import sys
import ConfigParser

'''
pythonHostConfig.ini
[HostAgent]
ipaddr = 192.168.0.138
port = 8080
url = /edCenter/module/welcome/getDataTestAction
datetime = timenu
cupname = cpunu
memname = memnu
diskname = disknu
'''
def rawconf():
    cf = ConfigParser.RawConfigParser()
    cf.read("pythonHostConfig.ini")
    ipaddr = cf.get("HostAgent", "ipaddr")
    port = cf.get("HostAgent", "port")
    url = cf.get("HostAgent", "url")
    datetime = cf.get("HostAgent", "datetime")
    cupname = cf.get("HostAgent", "cupname")
    memname = cf.get("HostAgent", "memname")
    diskname = cf.get("HostAgent", "diskname")

    print ipaddr
    print port
    print url
    print datetime
    print cupname
    print memname
    print diskname

def readCpuInfo():
    f = open('/proc/stat') 
    lines = f.readlines(); 
    f.close()
    for line in lines: 
        line = line.lstrip() 
        counters = line.split() 
        if len(counters) < 5: 
            continue
        if counters[0].startswith('cpu'):
            break
    total = 0
    for i in xrange(1, len(counters)): 
        total = total + float(counters[i])
    idle = float(counters[4])
    return {'total':total, 'idle':idle}


def calcCpuUsage(counters1, counters2):
    idle = counters2['idle'] - counters1['idle']
    total = counters2['total'] - counters1['total']
    return 100 - (idle / total) * 100


def getmem():
    with open('/proc/meminfo') as f:
        total = float(f.readline().split()[1])
        free = float(f.readline().split()[1])
        buffers = float(f.readline().split()[1])
        cache = float(f.readline().split()[1])
    # mem_use = total - free
    mem_use = total - free -buffers -cache
    return mem_use / total * 100


httpClient = None

try:
    while True:
        starttime = time.time()
        if __name__ == '__main__':
            rawconf()
            counters1 = readCpuInfo()
            time.sleep(1.9)
            timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
            counters2 = readCpuInfo()
            # print calcCpuUsage(counters1, counters2)
            timenu= "%s" %timenow
            cpunu = "%.1f" %calcCpuUsage(counters1, counters2)
            memnu = "%.1f" %getmem()

            params = urllib.urlencode(
                {datetime: timenu,
                 cupname: cpunu,
                 memname: memnu,
                 diskname: 'disk'
                }
            )

            headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
            zhongjian = time.time()
            httpClient = httplib.HTTPConnection( ipaddr, port, timeout=30)
            httpClient.request("POST", url, params, headers)
            
            response = httpClient.getresponse()
            # print response.status, response.reason
            print response.read()
            stoptime = time.time()
            print "总时间：%.1fs, 程序处理时间：%.1fs, http访问时间：%.1fs" %((stoptime - starttime),(zhongjian - starttime),(stoptime - zhongjian))
            print ""
            # print response.getheaders() #获取头信息

except Exception, e:
    print e
except KeyboardInterrupt:
    httpClient.close()
    exit()
finally:
    if httpClient:
        httpClient.close()
