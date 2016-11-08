#!/usr/bin/python  
  
import socket, sys
import random
import time

host = "localhost" 
port = 1987
#host = sys.argv[1]  
while True:   
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
	s.connect((host,port))
	msg = str(random.randint(1, 100))
	print "Data is: ",msg
	s.sendall("I Am Client1, Data is %s !" %msg) 
	time.sleep(3)



