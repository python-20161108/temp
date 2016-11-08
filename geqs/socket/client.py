import socket
import random
import time

address = ('127.0.0.1', 31500)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    while True:
        # msg = raw_input()
        msg = str(random.randint(1, 100))
        print msg
        if not msg:
            break
        s.sendto(msg, address)
        time.sleep(3)
except:
    s.close()
