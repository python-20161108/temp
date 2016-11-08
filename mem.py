import time

while True:
    timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    with open('/proc/meminfo') as f:
        total = float(f.readline().split()[1])
        free = float(f.readline().split()[1])
        buffers = float(f.readline().split()[1])
        cache = float(f.readline().split()[1])
    mem_use = total - free
    # mem_use = total - free -buffers -cache
    print "%s, mennu: %s" %(timenow, (format(mem_use/total, '.1%')))
    print "----------------------------------------------------"
    time.sleep(1)
