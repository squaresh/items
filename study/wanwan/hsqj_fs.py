#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fangshuai
# date:2021/xx/xx
# function:
import pymysql
import openpyxl
import datetime,time
from def1 import conf
from def2 import conf2
from openpyxl.styles import Color, Font, Alignment
db_gglog=pymysql.connect(host=conf.host,port=3306,
                      user=conf.user,passwd=conf.passwd,database=conf.database)

db_ads=pymysql.connect(host=conf.ahost,port=10004,
                      user=conf.auser,passwd=conf.apasswd,database=conf.adatabase)
hsqj_fs=openpyxl.load_workbook('/home/its_gs/fs/huqjtj/汇算清缴分时统计.xlsx')
now=datetime.datetime.now().strftime('%Y-%m-%d')
day=datetime.datetime.now().strftime('%Y年%m月%d日')
sheet=hsqj_fs['关键数据统计']
sheet.merge_cells('A1:E1')
sheet['A1']=f'{day}自然人电子税务局关键数据统计表'
align = Alignment(horizontal='center', vertical='center')
sheet
def dlrw():
    cursor_gglog=db_gglog.cursor()
    try:
        for i in range(0,24):
            sql=f"""SELECT COUNT(USERID) 
    FROM RZ_CZRZ 
    WHERE  CZURL IN ('/web/zh/v2/login/zhmmdl/txyzm','/web/zh/ifaa/auth/login','/web/zh/login/zhmmdl','/web/zh/scan/login/confirm')  
    AND `XGRQ` >= '{now} {i}:00:00' 
    AND `XGRQ` <= '{now} {i}:59:59'; """
            cursor_gglog.execute(sql)
            dlrwjg=cursor_gglog.fetchall()
            if dlrwjg:
                sheet[f'B{i+3}']=round(dlrwjg[0][0]/10000,2)
    except Exception as f :
        print(f)
def ywbl_app():
    cursor_ads=db_ads.cursor()
    try:
        for i in range(0,24):
            sql1=f"""select count(1) sl
                  from f_rt_SB_ZHSD_NDZXSB_ZB_qccx
                  where 
                        lrrq >='{now} {i}:00:00'
                    and lrrq <'{now} {i}:59:59'
                    and jyqd_dm = '11'
                    and (DLJGLX_DM is null or DLJGLX_DM = '');"""
            cursor_ads.execute(sql1)
            ywbl=cursor_ads.fetchall()
            if ywbl:
                sheet[f'C{i+3}']=round(ywbl[0][0]/10000,2)
    except Exception as f:
        print(f)
def ywbl_app_web():
    cursor_ads = db_ads.cursor()
    try:
        for i in range(0,24):
            sql2=f"""select count(1) sl
                      from f_rt_SB_ZHSD_NDZXSB_ZB_qccx
                      where 
                        lrrq >='{now} {i}:00:00'
                        and lrrq <'{now} {i}:59:59'"""
            cursor_ads.execute(sql2)
            ywbl=cursor_ads.fetchall()
            if ywbl:
                sheet[f'D{i+3}'] = round(ywbl[0][0]/10000,2)
    except Exception as f :
        print(f)
def main():
    dlrw()
    ywbl_app()
    ywbl_app_web()
    db_gglog.close()
    db_ads.close()
    hsqj_fs.save(f'/home/its_gs/fs/huqjtj/汇算清缴分时统计.{now}.xlsx')











