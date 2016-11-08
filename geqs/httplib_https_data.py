#!/usr/bin/env python
# coding=utf8

from httplib import HTTPSConnection
import json

ip = "192.168.0.150"
port = "8443"
data = "陈钦是坏人，大坏人"
method = "POST"
url = "/edCenter/module/welcome/getDataTestAction"
headers ={'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0'}

httpsconn = HTTPSConnection(ip, port).request(method, url, data, headers)
res = httpsconn.getresponse()
print res.status, res.reason, res.read()
