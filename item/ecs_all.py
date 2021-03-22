#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fangshuai
# date:2020/xx/xx
# !/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fangshuai
# date:2020/xx/xx
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkecs.request.v20140526.DescribeInstancesRequest import DescribeInstancesRequest
from aliyunsdkecs.request.v20140526.StopInstanceRequest import StopInstanceRequest
from aliyunsdkecs.request.v20140526.RebootInstanceRequest import RebootInstanceRequest
from aliyunsdkecs.request.v20140526.StartInstanceRequest import StartInstanceRequest
import json, time

now_time = time.strftime('%Y-%m-%d,%X', time.localtime())

client = AcsClient('', '', 'cn-hangzhou')

id_num=0
def InstancesRequest(num, Name):
    request = DescribeInstancesRequest()
    request.set_accept_format('json')
    request.set_PageNumber(num)
    request.set_PageSize(100)
    request.set_InstanceName(Name)

    response = client.do_action_with_exception(request)
    # python2:  print(response)
    try:
        ecs_stances = json.loads(str(response, encoding='utf-8'))
        ecs_stances1 = ecs_stances['Instances']['Instance']
        iid = []
        global id_num
        for i in ecs_stances1:
            InstanceName = i['InstanceName']
            # HostName = i['HostName']
            InstanceId = i['InstanceId']
            iid.append(InstanceId)
            print(InstanceName,end=',')
            id_num = id_num + 1
        return iid,id_num

    except Exception as f:
        print(f'实例获取发生错误：{f}')


def StopInstance(id):
    request = StopInstanceRequest()
    request.set_accept_format('json')
    # request.set_endpoint('ecs-internal.alicloud.its.tax.cn')  ####gda api接入点
    try:
        request.set_InstanceId(id)

        response = client.do_action_with_exception(request)
        # python2:  print(response)
        print(str(response, encoding='utf-8'))
    except Exception as f:
        print('实例id:', id)
        f = str(f)
        print('停止实例发生错误', f)
        error = '实例名称:' + id + '\\\报错信息:' + f + '\n'
        txt(error)


def reboot(id):
    request = RebootInstanceRequest()
    request.set_accept_format('json')
    # request.set_endpoint('ecs-internal.alicloud.its.tax.cn')  ####gda api接入点
    request.set_InstanceId(id)
    try:
        response = client.do_action_with_exception(request)
        response = json.loads(response)
        print(response)
    except Exception as f:
        print('实例id:', id)
        f = str(f)
        print('重启实例发生错误:', f)
        error = '实例名称:' + id + '\\\报错信息:' + f + '\n'
        txt(error)


def startecs(id):
    request = StartInstanceRequest()
    request.set_accept_format('json')
    # request.set_endpoint('ecs-internal.alicloud.its.tax.cn')  ####gda api接入点
    try:
        request.set_InstanceId(id)

        response = client.do_action_with_exception(request)
        print(str(response, encoding='utf-8'))
    except Exception as f:
        print('实例id:', id)
        f = str(f)
        print('启动实例发生错误', f)
        error = '实例名称:' + id + '\\\报错信息:' + f + '\n'
        txt(error)


def txt(error):
    with open(f'D:/pycharm/projects/learn/item/txt/ecs_error{now_time}.txt', mode='a+',encoding='utf-8') as kf:
        kf.write(error)


def select():
    Name = input('请输入ecs名称(仅支持通配符匹配):')
    iidd = []
    print('请确认你要操作的实例名称:')
    for i in range(1, 10):
        now_idd, now_id_num = InstancesRequest(i, Name)
        iidd.extend(now_idd)
    print(iidd)
    print(f'共计{now_id_num}台ecs')
    choose = input('请输入你要执行的操作(停止，启动，重启)输入其他则终止操作:')
    if choose == '停止':
        for id in iidd:
            StopInstance(id)
            time.sleep(1)
    elif choose == '启动':
        for id in iidd:
            startecs(id)
            time.sleep(1)
    elif choose == '重启':
        for id in iidd:
            reboot(id)
            time.sleep(1)
    else:
        print('终止变更')
if __name__ == '__main__':
    select()
