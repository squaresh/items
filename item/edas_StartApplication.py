#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fangshuai
# date:2020/xx/xx
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
import json
import time
client = AcsClient('VhxL6346jTLT4hfT','MTmxFadIUmFr7cto6Ia4Zpo25za2hI','cn-foshan-gjsw-d01')
def StartApplication(AppId):
    request = CommonRequest()
    request.set_accept_format('json')
    request.set_method('POST')
    request.set_protocol_type('https')  # https | http
    request.set_domain('ecs-internal.gdi.cloud.tax')
    request.set_version('2017-08-01')

    request.add_query_param('RegionId', "cn-foshan-gjsw-d01")
    request.add_query_param('AppId', AppId)
    request.add_header('Content-Type', 'application/json')
    request.set_uri_pattern('/pop/v5/changeorder/co_start')
    body = '''{}'''
    request.set_content(body.encode('utf-8'))

    response = client.do_action_with_exception(request)

    # python2:  print(response)
    print(str(response, encoding='utf-8'))
def appid(AppName):
    request = CommonRequest()
    request.set_accept_format('json')
    request.set_method('POST')
    request.set_protocol_type('https')
    request.set_domain('ecs-internal.gdi.cloud.tax')
    request.set_version('2017-08-01')

    request.add_query_param('RegionId', "cn-foshan-gjsw-d01")
    request.add_query_param('AppName', AppName)
    request.add_header('Content-Type', 'application/json')
    request.set_uri_pattern('/pop/v5/app/app_list')
    body = '''{}'''
    request.set_content(body.encode('utf-8'))

    response = client.do_action_with_exception(request)

    listAppaction=str(response, encoding = 'utf-8')
    appid_dict=json.loads(listAppaction)
    appid_list=appid_dict['ApplicationList']['Application']
    print(f'请确认需启动应用表列(包括重启):')
    for i in appid_list:
        name=i['Name']
        print(name)
    yes=input('请确认是否需要启动(包括重启)，输入yes则启动应用表列，输入其他则终止变更:')
    if yes=='yes':
        for i in appid_list:
            Appid=i['AppId']
            time.sleep(1)
            StartApplication(Appid)
    else:
        print('终止变更')

def main():
    AppName = input('请输入应用名称(可模糊匹配):')
    appid(AppName)
main()