#coding:utf8

import socket
import sys
import multiprocessing
import time

def test(port):
    ip = '192.168.0.1'
    port = int(port)
    print port
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.settimeout(0.5)
    print "正在扫描端口: %d" % port
    try:
        sk.connect((ip,port))
        print "Server %s port %d OK" % (ip,port)
    except Exception:
        print("Server {0:s} port {1:d} is not connected!".format(ip, port))
    sk.close()

if __name__ == '__main__':
    pool = multiprocessing.Pool(processes=20)
    for port in xrange(1, 65535):
        port = int(port)
        pool.apply_async(test, (port, ))
    pool.close()
    pool.join()
    print("Sub-process(es) done.")
