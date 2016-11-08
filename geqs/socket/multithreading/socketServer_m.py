#!/bin/evn python
#-*- coding: utf-8 -*-

import SocketServer
import os
       
class MyTCPHandler(SocketServer.BaseRequestHandler):

        def handle(self):
                print "欢迎: {}".format(self.client_address[0])
                while 1:
                        self.data = self.request.recv(1024).strip()
                        if not self.data:
                                print "再见: {}".format(self.client_address[0])
                                break
                        print "消息来自: {}".format(self.client_address[0]), "", "消息内容:", self.data
                        self.request.sendall(self.data.upper())
                        
if __name__ == "__main__":
        #执行前清理屏幕.
        os.system('clear')
        #打印执行前提示信息.
        print "socket多线程服务,正在监听中......"
        #设置监听主机和端口.
        HOST, POST = "localhost", 9999
        server = SocketServer.ThreadingTCPServer((HOST, POST), MyTCPHandler)
        server.serve_forever()