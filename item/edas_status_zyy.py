#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fangshuai
# date:2020/xx/xx
import json
import time
import openpyxl
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest

client = AcsClient('','', 'cn-hangzhou')


def listAppaction():
    request = CommonRequest()
    request.set_accept_format('json')
    request.set_method('POST')
    request.set_protocol_type('https')
    request.set_domain('edas.cn-hangzhou.aliyuncs.com')
    request.set_version('2017-08-01')

    request.add_query_param('RegionId', "cn-hangzhou")
    request.add_header('Content-Type', 'application/json')
    request.set_uri_pattern('/pop/v5/app/app_list')
    body = '''{}'''
    request.set_content(body.encode('utf-8'))

    response = client.do_action_with_exception(request)

    listAppaction = str(response, encoding='utf-8')
    appid_dict = json.loads(listAppaction)
    appid_list = appid_dict['ApplicationList']['Application']
    # print(appid_dict)
    for i in appid_list:
        AppId = i['AppId']
        # print(AppId)
        time.sleep(1)
        QueryApplicationStatus(AppId)


def QueryApplicationStatus(AppId):
    request = CommonRequest()
    request.set_accept_format('json')
    request.set_method('GET')
    request.set_protocol_type('https')  # https | http
    request.set_domain('edas.cn-hangzhou.aliyuncs.com')
    request.set_version('2017-08-01')

    request.add_query_param('RegionId', "cn-foshan-lhc-d01")
    request.add_query_param('AppId', AppId)
    request.add_header('Content-Type', 'application/json')
    request.set_uri_pattern('/pop/v5/app/app_status')
    body = '''{}'''
    request.set_content(body.encode('utf-8'))

    response = client.do_action_with_exception(request)

    ApplicationStatus = str(response, encoding='utf-8')
    ApplicationStatus_dict = json.loads(ApplicationStatus)
    try:
        ApplicationStatus_EcuList_list = ApplicationStatus_dict['AppInfo']['EcuList']['Ecu'][0]
    except:
        print('空应用', AppId)
        return
    InstanceId = ApplicationStatus_EcuList_list['InstanceId']
    try:
        ApplicationStatus_EccList_dict = ApplicationStatus_dict['AppInfo']['EccList']['Ecc'][0]
    except Exception as f:
        print('空应用', AppId)
        return

    Ip = ApplicationStatus_EccList_dict['Ip']
    # print(Ip)
    AppState = ApplicationStatus_EccList_dict['AppState']
    try:
        ApplicationStatus_Application_dict = ApplicationStatus_dict['AppInfo']['Application']
    except:
        print('空应用', AppId)
        return
    Name = ApplicationStatus_Application_dict['Name']
    RegionId = ApplicationStatus_Application_dict['RegionId']

    if AppState == 1:
        AppState = 'ECS停止'
        print(Name, AppState)
    elif AppState == 3:
        AppState = '应用异常(发布失败)'
        print(Name, AppState)
    elif AppState == 0:
        AppState = 'ecs已过期'
        print(Name, AppState)
    elif AppState == 7:
        print('应用正常')
    else:
        pass


if __name__ == '__main__':
    listAppaction()
