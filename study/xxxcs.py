#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fangshuai
# date:2020/xx/xx
# !/usr/bin/env python
# coding=utf-8
# 作用通过arms 获取应用qps值 默认获取当天最大pqs值，获取间隔1分钟
from aliyunsdkcore.client import AcsClient
import configparser
import argparse
import json
import datetime,time,os
import requests
path =os.getcwd()
abs_path=os.path.join(path,'txt/appid.ini')
def QueryMetricByPage(StartTime,Endtime,IntervalInSec,appname,pid):
    """
    rams模块
    :param StartTime: 开始时间
    :param Endtime: 结束时间
    :param IntervalInSec: 时间间隔
    :return: 无
    """
    try:
        param = {'startTime': StartTime,
                 'endTime': Endtime,
                 'intervallInSec': IntervalInSec,
                 'Metric': 'APPSTAT.DETAIL',
                 'Filters': [
                     {
                         "Key": "regionId",
                         "Value": "cn-shanghai"
                     },
                     {
                         "Key": "pid",
                         "Value": f'{pid}'
                     }
                 ],
                 'measures': ["rt", "count", "error"],
                 '_userId': '299407592184691422'}

        headers = {"Content-type": "application/x-www-form-urlencoded",
                   "Accept": "text/plain"}
        response = requests.post(url='http://100.63.136.98:8099/metric/Metric.json', data=param, headers=headers).json()
        response=json.loads(response)
        Items_dict=response['Data']['Items']
        max_count_dict=max(Items_dict, key=lambda dic: int(dic['count']))
        max_time=time.strftime("%Y-%m-%d %H:%M",(time.localtime(int(str(max_count_dict['date'])[:-3]))))
        max_count=max_count_dict['count']
        print('应用名:{},qps最大值:{},时间:{}'.format(appname,max_count,max_time))
    except Exception as f:
        print(f)

def chuancan():
    """
    读取appid 通过configparser配置文件(满足字典格式),参数key，value
    传参时间转换 通过argparse传入参数 在把时间转为时间撮，参数StartTime，Endtime，IntervalInSec
    :return:
    """
    conf = configparser.ConfigParser()
    conf.read(abs_path)
    pid_dict= conf['app_list']
    old7_time = ((datetime.datetime.now() - datetime.timedelta(days=0)).strftime("%Y-%m-%d 00:00"))
    now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    set_time = argparse.ArgumentParser()
    set_time.add_argument('-s',action='store',default=old7_time,help="-s表示开始时间为可选参数默认时间为7天,格式为:YYYY-MM-DD HH:mm")
    set_time.add_argument('-e', action='store', default=now_time,help="-e表示结束时间为可选参数")
    set_time.add_argument('-c',action='store',default=1,help='-c表示时间间隔，默认1分钟取一次')
    args = set_time.parse_args()
    for key,value in pid_dict.items():
        try:
            timeArray_s = time.strptime(str(args.s), "%Y-%m-%d %H:%M")
            StartTime = int(time.mktime(timeArray_s))
            timeArray_e = time.strptime(str(args.e), "%Y-%m-%d %H:%M")
            Endtime=int(time.mktime(timeArray_e))
            IntervalInSec=int(args.c)*60000

            QueryMetricByPage(StartTime, Endtime, IntervalInSec,key,value)
        except Exception as f:
            print('时间输入格式错误，请检查时间输入格式：默认格式YYYY-MM-DD HH:mm')
            print(f)

if __name__ == '__main__':
    chuancan()
