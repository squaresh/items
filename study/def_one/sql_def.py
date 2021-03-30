#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fangshuai
# date:2020/xx/xx
from faker import Faker
import random
faker=Faker()
val1=[]
for i in range(10):
    time1 = str(faker.date_time_between())
    name = faker.first_name_male()
    qps = str(random.randint(100, 1000))
    a=(name,time1,qps)
    val1.append(a)
val=val1
sql="insert into t_qps(app_name,peak_time,qps,lrrq) VALUES(%s,%s,%s,now())"
# print(val)
sq2="select id from t_qps"
