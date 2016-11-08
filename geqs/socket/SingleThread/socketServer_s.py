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
    print '欢迎:', addr

    while 1:
        data = conn.recv(1024)
        if not data:  
            print '再见:',addr
            break
        print "信息来自:", addr, "/", "消息内容:", data
        conn.sendall(data)
conn.close()
