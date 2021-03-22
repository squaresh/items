#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fangshuai
# date:2021/xx/xx
# function:
#!/usr/bin/env python
#coding=utf-8

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkecs.request.v20140526.AttachDiskRequest import AttachDiskRequest

client = AcsClient('<accessKeyId>', '<accessSecret>', 'cn-hangzhou')

def ecsgz(InstanceId,DiskId,Device):
    request = AttachDiskRequest()
    request.set_accept_format('json')

    request.set_InstanceId(InstanceId)
    request.set_DiskId(DiskId)
    request.set_Device(Device)

    response = client.do_action_with_exception(request)
    # python2:  print(response)
    print(str(response, encoding='utf-8'))
