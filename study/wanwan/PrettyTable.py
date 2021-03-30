#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fangshuai
# date:2020/xx/xx
from prettytable import PrettyTable
from prettytable import from_csv  ###读csv表格和满足scv格式的文件
from prettytable import from_html_one   ###读html文件
x = PrettyTable() ###定义引用这个函数 和pymysql configparse openpyxl argparser 一样

x.field_names = ["City name", "Area", "Population", "Annual Rainfall"] ###添加行的名字

x.add_row(["Adelaide", 1295, 1158259, 600.5]) ####添加第一列 add_columm()添加行的数据
x.add_row(["Brisbane", 5905, 1857594, 1146.4])
x.add_row(["Darwin", 112, 120900, 1714.7])
x.add_row(["Hobart", 1357, 205556, 619.5])
x.add_row(["Sydney", 2058, 4336374, 1214.8])
x.add_row(["Melbourne", 1566, 3806092, 646.9])
x.add_row(["Perth", 5386, 1554769, 869.4])
print(x)
with open('D:/pycharm/projects/learn/study/txt/pandas.csv', mode='r') as f: ####读取csv表格  和满足csv格式的文件
    x=from_csv(f)
print(x)
with open('D:/pycharm/projects/learn/study/txt/data.html',mode='r') as f1:   ####读取html文件
    f2=f1.read()
x1=from_html_one(f2)
print(x1)



