#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fangshuai
# date:2020/xx/xx
import pymysql
import configparser
conf=configparser.ConfigParser()
conf.read('D:/pycharm/projects/learn/study/txt/sc.ini')
host = conf['mysql']['host']
user = conf['mysql']['user']
passwd = conf['mysql']['passwd']
db = conf['mysql']['database']
# print(host)
# print(user)
# print(passwd)
# print(db)
mydb=pymysql.connect(host=host,
                     user=user,
                     passwd=passwd,
                     database=db)
cursor=mydb.cursor()
cursor.execute("select * from t_qps limit 10")
t_qps=cursor.fetchall()
# print(t_qps)
for i in t_qps:
    # pass
    print(i)


mydb.close()
