#!/bin/evn python
#-*- coding: utf-8 -*-

import socket
import time
import os

os.system('clear')

HOST = "localhost"
PORT = 9999

cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cli.connect((HOST, PORT))

while 1:    
    cli.sendall("Client2 is me!")
    data = cli.recv(1024)
    print "服务器返回内容:", repr(data)
    time.sleep(3)
cli.close()