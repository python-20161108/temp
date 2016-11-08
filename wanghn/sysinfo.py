

import time 


def readCpuInfo():
    f = open('/proc/stat') 
    lines = f.readlines(); 
    f.close()
    for line in lines: 
        line = line.lstrip() 
        counters = line.split() 
        if len(counters) < 5: 
            continue
        if counters[0].startswith('cpu'):
            break
    total = 0
    for i in xrange(1, len(counters)): 
        total = total + float(counters[i])
    idle = float(counters[4])
    return {'total':total, 'idle':idle}


def calcCpuUsage(counters1, counters2):
    idle = counters2['idle'] - counters1['idle']
    total = counters2['total'] - counters1['total']
    return 100 - (idle/total)*100


def getmem():
    with open('/proc/meminfo') as f:
        total = float(f.readline().split()[1])
        free = float(f.readline().split()[1])
        buffers = float(f.readline().split()[1])
        cache = float(f.readline().split()[1])
    mem_use = total - free
    # mem_use = total - free -buffers -cache
    print mem_use/total
    return mem_use/total*100


while True:
    if __name__ == '__main__': 
        counters1 = readCpuInfo()
        time.sleep(1)
        timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        counters2 = readCpuInfo()
        # print calcCpuUsage(counters1, counters2)
        print "time: %s, cpunu: %.1f, memnu: %.1f" %(timenow, (calcCpuUsage(counters1, counters2)), getmem())
        time.sleep(1)

