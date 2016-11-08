#!/usr/bin/python
# coding = utf-8

import socket, sys

host = 'localhost'  #bind to all interfaces
port = 1987

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(4)

print "Server is running on port %d" %port

while True:
	try:
		clientsock, clientaddr = s.accept()
		clientdata = clientsock.recv(1024)
		print "connection from: ", clientaddr[0], clientaddr[1], "data: ", clientdata
	except Exception, e:
		raise
	except KeyboardInterrupt:
		print "Ctrl + C, Exit!"
	else:
		pass
	finally:
		pass
