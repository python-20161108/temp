#!/bin/bash
date=`date +%Y%m%d_%-H:%-M:%S`
while :
    do
        #sleep 30
        pid1=`ps -ef|grep wanghn.py|grep -v grep`
        if [ -z "$pid1" ];
        then    
            python /root/python/wanghn.py &
            echo "$date 未检测到wanghn进程,现在启动wanghn..." >>/root/python/log.txt 
        fi
        pid2=`ps -ef|grep servicemonitor.py|grep -v grep`
        if [ -z "$pid2" ];
        then
            python /root/python/servicemonitor.py &
            echo "$date 未检测到servicemonitor进程,现在启动servicemonitor..." >>/root/python/log.txt
        fi
    done
