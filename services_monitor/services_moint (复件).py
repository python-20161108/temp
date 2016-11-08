#!/usr/bin/env python
#-*- coding: utf-8 -*-

from multiprocessing import Process
import sys, os
import time
import ConfigParser


def settings():
    cf = ConfigParser.RawConfigParser()
    cf.read("services_moint.ini")
    url = cf.get("HostAgent", "services")
    result = url.split(',')
    return result


def services():
    services = settings()
    proc_record = []
    try:
        for i in services:
            p = Process(name="serv_monitor")
            timenow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
            ret = os.popen('ps -C %s -o pid,cmd' %i).readlines()
            if len(ret) > 0:
                return timenow, 1
            elif len(ret) == 0:
                return timenow, 0

            p.start()
            # print p.pid, p.name
            proc_record.append(p)
        for p in proc_record:
            p.join()
            # print 'JOINED:', p, p.is_alive()

    except KeyboardInterrupt:
        exit(1)
    except:
        sys.exc_info()[1]


if __name__ == '__main__':
    while True:
        services()
        time.sleep(5)

