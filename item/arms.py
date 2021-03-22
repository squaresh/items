#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fangshuai
# date:2020/xx/xx
# !/usr/bin/env python
# coding=utf-8
# 作用 通过arms获取应用内存和cpu的最大值默认是7天时间间隔为1小时
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkarms.request.v20190808.QueryMetricByPageRequest import QueryMetricByPageRequest
import configparser
import argparse
import json
import datetime,time
client = AcsClient('', '', 'cn-shanghai')
def QueryMetricByPage(StartTime,Endtime,IntervalInSec,appname,pid):
    """
    rams模块
    :param StartTime: 开始时间
    :param Endtime: 结束时间
    :param IntervalInSec: 时间间隔
    :return: 无
    """
    try:
        request = QueryMetricByPageRequest()
        request.set_accept_format('json')

        request.set_EndTime(Endtime)
        request.set_Metric("appstat.host")
        request.set_Measuress(["systemCpuSystem", "systemCpuUser","systemMemUsed","systemLoad"])
        request.set_IntervalInSec(IntervalInSec)
        request.set_Filterss([
            {
                "Key": "regionId",
                "Value": "cn-shanghai"
            },
            {
                "Key": "pid",
                "Value": f'{pid}'
            }
        ])
        request.set_StartTime(StartTime)
        request.set_PageSize(3000)
        response = client.do_action_with_exception(request)
        response=json.loads(str(response, encoding='utf-8'))
        Items_dict=response['Data']['Items']
        Cpu=[]
        MemUsed=[]
        for i in Items_dict:
            MemUsed.append((float(i['systemMemUsed'])/1024/1024/1024))
            Cpu.append((float(i['systemCpuUser'])+float(i['systemCpuSystem'])))
        avg_MemUsed=round((sum(MemUsed)/len(MemUsed)),2)
        avg_Cpu=round((sum(Cpu)/len(Cpu)),2)
        print('{}的内存的平均值:{},内存最大值:{}'.format(appname,avg_MemUsed,round(max(MemUsed),3)))
        print('{}的cpu的平均值:{},cpu最大值:{}'.format(appname,avg_Cpu,round(max(Cpu),3)))


    except Exception as f:
        print(f)
def chuancan():
    """
    读取appid 通过configparser配置文件(满足字典格式),参数key，value
    传参时间转换 通过argparse传入参数 在把时间转为时间撮，参数StartTime，Endtime，IntervalInSec
    :return:
    """
    conf = configparser.ConfigParser()
    conf.read('D:/pycharm/projects/learn/study/txt/appid.ini')
    pid_dict= conf['app_list']
    old7_time = ((datetime.datetime.now() - datetime.timedelta(days=7)).strftime("%Y-%m-%d %H:%M"))
    now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    set_time = argparse.ArgumentParser()
    set_time.add_argument('-s',action='store',default=old7_time,help="-s表示开始时间为可选参数默认时间为7天,格式为:YYYY-MM-DD HH:mm")
    set_time.add_argument('-e', action='store', default=now_time,help="-e表示结束时间为可选参数")
    set_time.add_argument('-c',action='store',default=1,help='-c表示时间间隔，默认1个小时')
    args = set_time.parse_args()
    for key,value in pid_dict.items():
        try:
            timeArray_s = time.strptime(str(args.s), "%Y-%m-%d %H:%M")
            StartTime = int(time.mktime(timeArray_s))
            timeArray_e = time.strptime(str(args.e), "%Y-%m-%d %H:%M")
            Endtime=int(time.mktime(timeArray_e))
            IntervalInSec=int(args.c)*3600000

            QueryMetricByPage(StartTime, Endtime, IntervalInSec,key,value)
        except Exception as f:
            print('时间输入格式错误，请检查时间输入格式：默认格式YYYY-MM-DD HH:mm')
            print(f)

if __name__ == '__main__':
    chuancan()







