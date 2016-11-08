#!/usr/bin/python  
# coding=utf-8

import socket
# import sys
import random
import time

# 参数传递方式
# serv_host = sys.argv[1]
# serv_port = sys.argv[2]
# monitoring_frequency = sys.argv[3]

# 配置传递方式
serv_host = "localhost" # ip address 
serv_port = 1987 # 1-65535
monitoring_frequency = 3 # second

try:
	while True:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP mode
		s.connect((serv_host, serv_port))
		msg = str(random.randint(1, 100)) # 产生随机数
		print "Data is: ", msg
		s.sendall("I Am Client1, Data is %s !" %msg)
		time.sleep(monitoring_frequency)
#except Exception, e:
#	raisel
except	socket.error:
	print "server %s not connect!" %serv_host

except	KeyboardInterrupt:
		s.close()
		system.exit(1)
	print "Ctrl + C, Exit!"
except:
	s.close()
