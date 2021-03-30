#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fangshuai
# date:2020/xx/xx
##适用于一个sql对应一行 通用脚本
from openpyxl import load_workbook
import time
import pymysql

fxgl = pymysql.connect(host='drdsusrzlag55u4w.drds.bj.cloud.tax',
                       user='etax_fxgl_ops_ro',
                       passwd='9IBk1xC2mFYBJctX',
                       database='fxgl')
cursor_fx = fxgl.cursor()

book = load_workbook('/home/its_gs/fs/python/yunwei_tool/事后抽查业务办理情况监控脚本.xlsx')
dm_list = ['F01', 'F02', 'F03', 'F04', 'F05', 'F06', 'F07', 'F08', 'F09', 'F10',
           'F11', 'F12', 'F13', 'F14', 'F15', 'F16', 'F17', 'F19', 'F20', 'F21', 'F22', 'F23', 'F24']
######匹配的列表
def sql_mmdy(dm_list):
    sheet = book['口径']
    keys = []
    values = []
    for i in sheet['H']:
        if i.value in dm_list:
            keys.append(i.value)
            values.append(sheet[f'J{i.row}'].value)
    return keys, values


keys, values = sql_mmdy(dm_list)
sql_dict = dict(zip(keys, values))  ###把模板中的sql做成字典 记住keys要在列表内


def qushu(sql_dict,cursor):
    sheet_mg = book['全国']
    for i in sheet_mg['E']:  ###确定行的位置
        if str(i.value).strip() in dm_list:   ###判断写数据的execlkeys值是否在
            try:
                cursor.execute(sql_dict[i.value])
                sql1 = cursor.fetchall()
                if sql1:
                    for a in sql1:
                        if len(a) == 2:    ###判断sql输出长度 以确定位置
                            for shuju in sheet_mg[f'G{i.row}':'G81']:  ####字段列 ---输出是元组
                                shuju = shuju[0]  ###取元组的数据
                                if str(a[0]) == str(shuju.value).strip():   ###数据行和目标单元格匹配
                                    sheet_mg[f'H{shuju.row}'] = a[1]  ####数据列
                                    break
                        elif len(a) == 3:
                            if a[0] == '新增扫描':
                                for shuju in sheet_mg[f'G29':'G36']:  ####字段列
                                    shuju = shuju[0]
                                    if str(a[1]) == str(shuju.value).strip():
                                        sheet_mg[f'H{shuju.row}'] = a[2]  ####数据列
                                        break
                            if a[0] == '更新扫描':
                                for shuju in sheet_mg[f'G37':'G44']:  ####字段列
                                    shuju = shuju[0]
                                    if str(a[1]) ==str(shuju.value).strip():   ###数据行和目标单元格匹配
                                        sheet_mg[f'H{shuju.row}'] = a[2]  ####数据列
                                        break

                        elif len(a) == 1:
                            sheet_mg[f'H{i.row}'] = a[0]
                        else:
                            print('存数发出错误')
            except:
                print('链接数据库发生错误')

def close():
    fxgl.close()
    book.save('/home/its_gs/fs/python/yunwei_tool/sc.xlsx')

if __name__ == '__main__':
    qushu(sql_dict,cursor_fx)
    close()
