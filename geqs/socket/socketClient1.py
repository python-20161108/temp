#!/bin/evn python
#-*- coding: utf-8 -*-

import socket
import time

HOST = "192.168.88.1"
PORT = 843

while 1:
    cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cli.connect((HOST,PORT))
    cli.sendall('Client is me!')
    data = cli.recv(1024)
    time.sleep(1)
    print "客户端攻击信息:",repr(data)
#    cli.close()

