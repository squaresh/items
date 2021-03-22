#!/usr/bin/env python
#coding=utf-8
#writer:fangshuai

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkecs.request.v20140526.StopInstanceRequest import StopInstanceRequest
import time
from config.seting import ak,sk
def StopInstance(id):
    client = AcsClient(ak, sk, 'cn-foshan-lhc-d01')

    request = StopInstanceRequest()
    request.set_accept_format('json')
    request.set_endpoint('ecs-internal.alicloud.its.tax.cn')  ####gda api接入点
    try:
        request.set_InstanceId(id)

        response = client.do_action_with_exception(request)
        # python2:  print(response)
        print(str(response, encoding='utf-8'))
    except Exception as f:
        print('实例id:', id)
        print(f)

with open('/home/its_gs/fs/yunwei/txt/id_stop_list',mode='r+') as f:
    for i in f.readlines():
        a=i.replace('\n','')
        id_list=a.split(',')
        for id in id_list:
            if id !='':
                StopInstance(id)
                time.sleep(1)