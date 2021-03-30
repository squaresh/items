#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fangshuai
# date:2020/xx/xx
import pymysql
from study.def_one import argparse_def
import time
import argparse
now_time=time.strftime('%Y-%m-%d %X',time.localtime())
last_time=time.strftime('%Y-01-01-01 00:00:00',time.localtime())
set_time=argparse.ArgumentParser()
set_time.add_argument('-s',help='开始时间',default='good')
set_time.add_argument('-e',help='结束时间',default='good1')
sett_time=set_time.parse_args() ####set_time.parse_args().__dict__转成字典
if sett_time.s and sett_time.e:
    try:
        sql=f"SELECT * from t_qps WHERE peak_time>'{sett_time.s}' and lrrq<'{sett_time.e}'"
    except:
        print('输入时间格式错误,参考:2020-10-11 20:20')
else:
    sql=f"SELECT * from t_qps WHERE peak_time>'{last_time}'and lrrq<'{now_time}'"
mydb=pymysql.connect(host='rm-bp1p689196a0p9vr2co.mysql.rds.aliyuncs.com',
                     user='fs_cs',
                     passwd='Admin@123',
                     database='fs_cs')
cursor=mydb.cursor()
try:
    cursor.execute(sql)
    data=cursor.fetchall()
    for i in data:
        print(i)
except:
    print('查询遇到失败')

