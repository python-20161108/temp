#!/usr/bin/python

import socket, sys

textport = "1987"
host = "localhost"
#host = sys.argv[1]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    port = int(textport)
except ValueError:
    print "Ettot port"
    port = socket.getservbyname(textport, 'udp')

s.connect((host, port))
s.sendall("I am client")

while 1:
    buf = s.recv(2048)
    if not len(buf):
        break
    print buf
    #sys.stdout.write(buf)

s.close()
