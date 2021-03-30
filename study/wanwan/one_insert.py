#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fangshuai
# date:2020/xx/xx
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fangshuai
# date:2020/xx/xx
import pymysql
from study.def_one import sql_def
mydb=pymysql.connect(host='rm-bp1p689196a0p9vr2co.mysql.rds.aliyuncs.com',
                     user='fs_cs',
                     passwd='Admin@123',
                     database='fs_cs')
cursor=mydb.cursor()      ##使用默认游标 返回以元组的形式
#cursor=mydb.cursor(pymysql.cursors.DictCursor)   #定义游标 返回以字典的形式返回
# try:
#     cursor.executemany(sql_def.sql, sql_def.val)
#     mydb.commit()
#     print("成功写入数据")
# except:
#     print('遇到未知错误已回退')
#     mydb.rollback()
cursor.execute(sql_def.sq2)
t_qps=cursor.fetchall()
if t_qps:
    # print(t_qps)
    for i in t_qps:
        print(i)
        print(i[0])

        # pass
        # print(i)
        # a = str(i[0])
        # print(a, type(a))
else:
    print(0)

# print(t_qps)
# t_qps1=t_qps[0][0]
# print(t_qps1)
# a='dsa'
# b=str(a)
# print(b,type(b))



mydb.close()
