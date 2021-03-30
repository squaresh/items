#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fangshuai
# date:2020/xx/xx
import time

now=time.localtime()
time1=time.strftime('%Y-%m-%d 00:00',now)
time2=time.strftime('%Y-%m-%d %X',now)
val=(time1,time2)
sql1="select sum(status),subject from alerts where  from_unixtime(clock)>'{}' and from_unixtime(clock)<'{}' and sendto like '%1535003180%' group by subject having subject like '%Problem%'".format(time1,time2)
sql2="select sum(status),subject from alerts where  from_unixtime(clock)>'{}' and from_unixtime(clock)<'{}' and sendto like '%1535003180%' group by subject having subject like '%Resolved%'".format(time1,time2)
print(sql1)
print(sql2)