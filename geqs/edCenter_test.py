#!/usr/bin/python  
# coding=utf-8


import urllib
import httplib 
test_data = {'ServiceCode':'aaaa','b':'bbbbb'}
test_data_urlencode = urllib.urlencode(test_data)

requrl = "http://192.168.0.150:8080/edCenter/login.html"
headerdata = {"Host":"192.168.0.150"}
conn = httplib.HTTPConnection("192.168.0.150:8080")
conn.request(method="POST", url=requrl, body=test_data_urlencode, headers = headerdata)  
response = conn.getresponse()

res= response.read()

print res