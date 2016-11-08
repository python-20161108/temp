#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import json

from django.http import HttpResponse


def json_Response(request):
    if request.method == 'POST':
        # 将接收到的json数据转义
        req = json.loads(request.body)
        print(request.body)
        print(req)
        return HttpResponse(request.body)
    else:
        print('没有接收到数据')
