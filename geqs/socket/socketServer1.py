#!/bin/evn python
#-*- coding: utf-8 -*-

import socket

HOST =''
PORT =5000
srv = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
srv.bind((HOST,PORT))
srv.listen(1)

while 1:
    conn,addr = srv.accept()
    print '你好！ by:',addr
    data = conn.recv(1024)
    if not data: break
    print "访问地址来自：", addr,"/","发送数据内容：", data
    conn.sendall(data)
conn.close()
