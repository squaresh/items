# # 2 3 选择排序
# a=[3,8,12,9,2,8,6,1]
# for i in range(len(a)):
#     # print(i)
#     for j in range(i+1,len(a)):
#         if a[i]<a[j]:
#             a[i],a[j]=a[j],a[i]   ###选择排序 原理就是循环一次找出最小 或者最大的那个（通过换位）
#             print(a[i],a[j])       ####循环一次确定一个位置的数字的大小，然后再找另一个
#     # print(a)
# print(a)
# a=[[11,'gg'],[22,'gg'],[33,'ff']]###列表和选择可以转成字典只要满足成对出现
# b=[(11,'gg'),(22,'gg'),(33,'ff')]
# c=((11,'gg'),(22,'gg'),(33,'ff'))
#
# print(dict(c))
# import mysql.connector
# mydb= mysql.connector.connect(host="rm-bp1p689196a0p9vr2co.mysql.rds.aliyuncs.com",
#                               user="csb_gnhj",
#                               passwd="Servyou2019",
#                               database="csb_gnhj")
# data1=mydb.cursor()
# sql="select * from csb_aliyun_cn_hangzhou_kjtweb_service_info"
# data1.execute(sql)
# data=data1.fetchall()
# # print(data)
# for i in data:
#     with open('data',mode='a+') as f:
#         f.write(str(i)+'\n')
#     print(i)
# mydb.close()
# import time
#
# now=time.localtime()
# time1=time.strftime('%Y-%m-%d 00:00',now)
# time2=time.strftime('%Y-%m-%d %X',now)
# val=(time1,time2)
# sql1="select sum(status),subject from alerts where  from_unixtime(clock)>%s and from_unixtime(clock)<%s and sendto like '%1535003180%' group by subject having subject like '%Problem%'"
# sql2="select sum(status),subject from alerts where  from_unixtime(clock)>%s and from_unixtime(clock)<%s and sendto like '%1535003180%' group by subject having subject like '%Resolved%'"
####日志打印模块
# import logging ##打印日志模块
# root = logging.getLogger('dev') ##指定记录器的明名称'dev' 下面可以设置打印这个名称(便于找那个)
# root.setLevel(logging.INFO) ##设置此记录器的打印的日志级别 info(意思说info级别下的日志都可打印)
#
# log_format = '%(asctime)s %(name)s :%(levelname)s:%(filename)s: %(message)s' ###设置需要打印的固定内容
# logging.basicConfig(filename="test.log", format=log_format) ###filename指定打印位置和文件名 format指定打印内容
#
# # incident happens
# try:
#     a=dsad
# except Exception as f:
#     root.error(f,exc_info=True) ###这些函数一直运行到引发异常时为止。 堆栈跟踪包含在exc_info选项中
# error_message = 'authentication failed'
#
# root.error(f'error: {error_message}')
# root.critical('nisyigeda')
# root.warning('good')
# root.info('bad')
#!/usr/bin/env python
#coding=utf-8

import requests
