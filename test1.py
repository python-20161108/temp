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
        total = total + float('%0.1f' %counters[i])
    idle = float('%0.1f' %counters[4]) 
    return {'total':total, 'idle':idle}


def calcCpuUsage(counters1, counters2):
    idle = counters2['idle'] - counters1['idle']
    total = counters2['total'] - counters1['total']
    return 100 - (idle*100/total)

while True:
    if __name__ == '__main__': 
        counters1 = readCpuInfo()
        time.sleep(1)
        counters2 = readCpuInfo()
        print calcCpuUsage(counters1, counters2)

