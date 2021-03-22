#!/usr/bin/env python
#coding=utf-8
#writer=fangshuai

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkecs.request.v20140526.StartInstanceRequest import StartInstanceRequest
import time
from config.seting import ak,sk

def startecs(id):
    client = AcsClient(ak, sk, 'cn-foshan-lhc-d01')
    request = StartInstanceRequest()
    request.set_accept_format('json')
    request.set_endpoint('ecs-internal.alicloud.its.tax.cn')  ####gda api接入点
    try:
        request.set_InstanceId(id)

        response = client.do_action_with_exception(request)
        print(str(response, encoding='utf-8'))
    except Exception as of:
        print('实例id:',id)
        print(of)
with open('/home/its_gs/fs/yunwei/txt/id_start_list',mode='r+') as f:
    for i in f.readlines():
        a=i.replace('\n','')
        id_list=a.split(',')
        for id in id_list:
            if id !='':
                startecs(id)
                time.sleep(1)
            else:
                print('表列为空')
