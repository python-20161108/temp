#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import urllib2


posturl = "https://192.168.0.150:8443/edCenter/module/welcome/getDataTestAction"

postData = {'userName': 'admin',
            'password': '12345678aA',
            }

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:14.0) Gecko/20100101 Firefox/14.0.1',
           'Referer': '******'}
postData = urllib.urlencode(postData)
try:
    request = urllib2.Request(posturl, postData, headers)
    print(request)
    response = urllib2.urlopen(request)

    text = response.read()
    print(text)
except urllib2.HTTPError as e:
    print e
    pass
