#!/usr/bin/python

import socket, sys

host = 'localhost'  #bind to all interfaces
port = 1987

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(4)

print "Server is running on port %d" % port
while 1:
    try:
        clientsock, clientaddr = s.accept()
    except KeyboardInterrupt: # Press "Ctrl + C" to quit
        print "Quit"
        sys.exit(1)
    print "connection from ", clientaddr
    msg = clientsock.recv(1024)
    if not msg:
        break
    clientsock.sendall("Received " + msg)
    clientsock.close()

s.close()
