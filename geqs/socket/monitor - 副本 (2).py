#!/usr/bin/env python
#-*- coding: utf-8 -*-

#import os
import MySQLdb as mysql
import socket
import fcntl
import struct
import platform
import time
import random

db = mysql.connect(user="root",passwd="12345678mM",db="jkpt",host="localhost")
db.autocommit(True)
cur = db.cursor()

tmp_time = 0

def info():
    global tmp_time
    if tmp_time > 0:    
        #查询数据库；
        sql = 'select * from jkpt_hoststatus where timemu>%s' %(tmp_time/1000)
    else:
        sql = 'select * from jkpt_hoststatus'
    cur.execute(sql)
    
    #打印调试信息；
    print sql
    print tmp_time
    
while True:
    time.sleep(3)
    info()
