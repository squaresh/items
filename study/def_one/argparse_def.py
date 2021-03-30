#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fangshuai
# date:2020/xx/xx
#####此脚本不能配其他脚本调用因为argparse模块定义的参数(命令行输入的)无法直接到直接调用的脚本
import time
import argparse
now_time=time.strftime('%Y-%m-%d %X',time.localtime())
last_time=time.strftime('%Y-01-01-01 00:00:00',time.localtime())
set_time=argparse.ArgumentParser()
set_time.add_argument('-s',help='开始时间')
set_time.add_argument('-e',help='结束时间')
sett_time=set_time.parse_args()
if sett_time.s and sett_time.e:
    try:
        sql=f"SELECT * from t_qps WHERE peak_time>'{sett_time.s}' and lrrq<'{sett_time.e}'"
    except:
        print('输入时间格式错误,参考:2020-10-11 20:20')
else:
    sql=f"SELECT * from t_qps WHERE peak_time>'{last_time}'and lrrq<'{now_time}'"