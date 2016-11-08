#!/bin/evn python
#-*- coding: utf-8 -*-

import socket
import os

os.system('clear')

HOST = "localhost"
PORT = 9999

cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cli.connect((HOST, PORT))

while 1:
    cmd = raw_input("请输入命令:").strip()
    if len(cmd) == 0:continue
    cli.sendall(cmd)
    data = cli.recv(1024)
    print "服务器返回内容:", repr(data)
cli.close()
