#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : ecs_reboot.py
# Author: chenweizhang
# Date  : 2020/9/9
from json import loads
import time
from aliyunsdkcore.acs_exception.exceptions import ServerException, ClientException
from aliyunsdkcore.client import AcsClient
from aliyunsdkecs.request.v20140526.RebootInstanceRequest import RebootInstanceRequest
from config.seting import ak,sk
def reboot(InstanceId):
    client = AcsClient(ak,sk,'cn-foshan-lhc-d01')
    request = RebootInstanceRequest()
    request.set_accept_format('json')
    request.set_endpoint('ecs-internal.alicloud.its.tax.cn')  ####gda api接入点
    request.set_InstanceId(InstanceId)
    try:
        response = client.do_action_with_exception(request)
        response=loads(response)
        print(response)
    except ServerException as e:
        print("服务端异常:httpstatus[%s],codd[%s],msg[%s]" % (e.get_http_status(),
                                                               e.get_error_code(),
                                                               e.get_error_msg()))
    except ClientException as e:

        print("sdk端错误:codd[%s],msg[%s]" % (e.get_error_code(), e.get_error_msg()))

with open('/home/its_gs/fs/yunwei/txt/id_reboot_list',mode='r+') as f:
    for i in f.readlines():
        a=i.replace('\n','')
        id_list=a.split(',')
        for id in id_list:
            if id !='':
                reboot(id)
                time.sleep(1)