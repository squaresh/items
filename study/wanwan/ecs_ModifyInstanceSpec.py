#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fangshuai
# date:2020/xx/xx
###升降配按量付费ecs实例
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkecs.request.v20140526.ModifyInstanceSpecRequest import ModifyInstanceSpecRequest
from config.seting import ak, sk
import time

client = AcsClient(ak, sk, 'cn-foshan-lhc-d01')


def ModifyInstanceS(id, InstanceType):
    request = ModifyInstanceSpecRequest()
    request.set_accept_format('json')
    request.set_endpoint('ecs-internal.alicloud.its.tax.cn')
    try:
        request.set_InstanceId(id)
        request.set_InstanceType(InstanceType)

        response = client.do_action_with_exception(request)
        # python2:  print(response)
        print(str(response, encoding='utf-8'))
    except Exception as f:
        print(f)


with open('/home/its_gs/fs/yunwei/txt/id_jiangpei_list', mode='r') as f:
    InstanceType = input('请输入你要变更的实例规格:')
    for i in f.readlines():
        a = i.replace('\n', '')
        id_list = a.split(',')
        for id in id_list:
            if id != '':
                ModifyInstanceS(id, InstanceType)
                time.sleep(6)
