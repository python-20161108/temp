#!/usr/bin/python  
  
import socket, sys  

host = "localhost" 
port = 1987  
#host = sys.argv[1]  
  
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
  
try:  
    s.connect((host,port))  
except socket.error:  
    print "Error connecting server %s " % host  
    sys.exit(1)  
  
s.sendall("I am client")  
  
while 1:  
    buf = s.recv(2048)  
    if not len(buf):  
        break  
    print buf  
    #sys.stdout.write(buf)  
  
s.close() 
