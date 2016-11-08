#!/bin/evn python
#-*- coding: utf-8 -*-

import socket
import time

HOST = "localhost"
PORT = 5000

cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cli.connect((HOST,PORT))

while 1:    
    cli.sendall('Client is me!')
    data = cli.recv(1024)
    time.sleep(2)
    print "客户端信息:",repr(data)
cli.close()

