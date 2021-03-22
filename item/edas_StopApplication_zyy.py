#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fangshuai
# date:2020/xx/xx
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
import json
import time
client = AcsClient('LTAI4GDDng9o1Jcr7NXMyR75','esCq8FBLqFVky0EupSp1Abr9MUycaH','cn-hangzhou')
def StopApplication(AppId):
    request = CommonRequest()
    request.set_accept_format('json')
    request.set_method('POST')
    request.set_protocol_type('http') # https | http
    request.set_domain('edas.cn-hangzhou.aliyuncs.com')  ###api 接入点
    request.set_version('2017-08-01')

    request.add_query_param('RegionId', "cn-hangzhou")
    request.add_query_param('AppId', AppId)
    request.add_header('Content-Type', 'application/json')
    request.set_uri_pattern('/pop/v5/changeorder/co_stop')
    body = '''{}'''
    request.set_content(body.encode('utf-8'))

    response = client.do_action_with_exception(request)

    # python2:  print(response)
    print(str(response, encoding = 'utf-8'))
def appid():
    request = CommonRequest()
    request.set_accept_format('json')
    request.set_method('POST')
    request.set_protocol_type('http')
    request.set_domain('edas.cn-hangzhou.aliyuncs.com')
    request.set_version('2017-08-01')

    request.add_query_param('RegionId', "cn-hangzhou")
    # request.add_query_param('AppId',)
    request.add_header('Content-Type', 'application/json')
    request.set_uri_pattern('/pop/v5/app/app_list')
    body = '''{}'''
    request.set_content(body.encode('utf-8'))

    response = client.do_action_with_exception(request)

    listAppaction=str(response, encoding = 'utf-8')
    appid_dict=json.loads(listAppaction)
    appid_list=appid_dict['ApplicationList']['Application']
    appname=input('请输入应用名称(可模糊匹配):')
    print(f'请确认需停止应用表列:')
    get_appid_list=[]
    for i in appid_list:
        name=i['Name']
        if appname in name:
            print(name)
            get_appid_list.append(i['AppId'])
    yes=input('请确认是否需要停止，输入yes则停止应用表列，输入其他则终止变更:')
    if yes=='yes':
        for i in get_appid_list:
            print(i)
            time.sleep(1)
            StopApplication(i)
    else:
        print('终止变更')

def main():
    appid()
main()