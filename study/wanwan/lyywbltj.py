#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fangshuai
# date:2020/xx/xx
from openpyxl import Workbook
from openpyxl import load_workbook
import time
import pymysql

now_time = time.strftime('%Y-%m-%d', time.localtime())

fxgl = pymysql.connect(host='xxx',
                       user='xxx',
                       passwd='xx',
                       database='sgzl')
cursor = fxgl.cursor()
book = load_workbook('D:/pycharm/projects/learn/item/execl/事后抽查业务办理情况监控脚本.xlsx')