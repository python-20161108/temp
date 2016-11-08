#!/usr/bin/python

import socket, sys

host = ''  #bind to all interfaces
port = 1987

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))

print "Server is running on port %d" % port
while 1:
    try:
        msg, remote_addr = s.recvfrom(1024)
    except KeyboardInterrupt: # Press "Ctrl + C" to quit
        print "Quit"
        sys.exit(1)
    if not msg:
        break
    s.sendto("Received " + msg, remote_addr)

s.close()
