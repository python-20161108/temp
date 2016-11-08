#!/usr/bin/env python
#-*- coding: utf-8 -*-

#import os
import random
import struct
import time

import MySQLdb as mysql
import fcntl

import platform
import socket

db = mysql.connect(user="root",passwd="12345678mM",db="jkpt",host="localhost")
db.autocommit(True)
cur = db.cursor()

    
def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

def getinfo():
    #读取主机名称；
    myname = socket.getfqdn(socket.gethostname(  ))
    
    #读取IP地址；
    def myaddr():
        if len(platform.system()) == 7:  
            addr = socket.gethostbyname(myname)  #返回Windows IP地址
            return addr
        else:
            addr = get_ip_address("eth0")  #返回Linux IP地址
            return addr
        
    #读取内存使用；        
    def meminfo():
        with open('/proc/meminfo') as f:
            total = int(f.readline().split()[1])
            free = int(f.readline().split()[1])
            buffers = int(f.readline().split()[1])
            cache = int(f.readline().split()[1])
        mem_use = (total-free-buffers-cache)/1024
        return mem_use
    
    jinggao = random.randint(50,100)
    
    #读取当前时间；
    t = int(time.time())*1000
    
    #导入数据库；
    sql = 'insert into jkpt_hoststatus (hostname,ipaddr,timenu,memory,jinggao) value (\'%s\',\'%s\',\'%s\',\'%s\',\'%s\')'%(myname,myaddr(),t,meminfo(),jinggao)
    cur.execute(sql)
    
    #打印调试信息；
    print myname,myaddr(),t,meminfo(),jinggao
    
while True:
    time.sleep(3)
    getinfo()