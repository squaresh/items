#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fangshuai
# date:2021/xx/xx
# function:
import pymysql
from def1 import conf
from def2 import conf2
db_gglog=pymysql.connect(host=conf.host,port=3306,
                      user=conf.user,passwd=conf.passwd,database=conf.database)

db_ads=pymysql.connect(host=conf.ahost,port=10004,
                      user=conf.auser,passwd=conf.apasswd,database=conf.adatabase)
def dlrw():
    cursor_gglog=db_gglog.cursor()
    try:
        sql=f"""SELECT '分时统计登录人次' as 类型,round(COUNT(USERID) /10000,1) as 数量
FROM RZ_CZRZ
WHERE CZURL IN('/web/zh/v2/login/zhmmdl/txyzm', '/web/zh/ifaa/auth/login', '/web/zh/login/zhmmdl', '/web/zh/scan/login/confirm')
AND  XGRQ >= date_format((date_sub(now(),interval 1 hour)),'%y-%m-%d %H:00:00')
AND `XGRQ`< date_format(now(),'%y-%m-%d %H:00:00')
union ALL
SELECT '当天累计登录人次'as 类型,round(COUNT(USERID) /10000,1) as 数量
FROM RZ_CZRZ
WHERE CZURL IN('/web/zh/v2/login/zhmmdl/txyzm', '/web/zh/ifaa/auth/login', '/web/zh/login/zhmmdl', '/web/zh/scan/login/confirm')
AND `XGRQ`>= date_format(now(),'%y-%m-%d 00:00:00')
AND `XGRQ`< date_format(now(),'%y-%m-%d %H:00:00');"""
        cursor_gglog.execute(sql)
        dlrwjg=cursor_gglog.fetchall()
        for i in dlrwjg:
            print()
    except Exception as f:
        print(f)
def ywbl_app():
    cursor_ads=db_ads.cursor()
    try:
        sql1=f"""select  'APP 办理' as 类型，round(count(1) /10000,1) as 数量
from f_rt_SB_ZHSD_NDZXSB_ZB_qccx
where date_format(lrrq,'%y%m%d%H') = date_format((date_sub(now(),interval 1 hour)),'%y%m%d%H')
and jyqd_dm= '11'
and(DLJGLX_DM is null
or DLJGLX_DM= '')
union all
#######################################################################################################
#3.业务办理数（APP+ WEB 单位：万笔）
select 'APP+WEB 办理'  as 类型，round(count(1)/10000,1) as 数量
from f_rt_SB_ZHSD_NDZXSB_ZB_qccx
where date_format(lrrq,'%y%m%d%H') = date_format((date_sub(now(),interval 1 hour)),'%y%m%d%H')
union all
#当天全量
select 'APP+WEB当天累计办理' as 类型，round(count(1) /10000,1) as 数量
from f_rt_SB_ZHSD_NDZXSB_ZB_qccx
where 
if(
date_format(now(),'%Y%m%d %H') != date_format(now(),'%Y%m%d 00'),

date_format(lrrq,'%y%m%d')>= date_format(now(),'%y%m%d')
and date_format(lrrq,'%y%m%d%H')< date_format(now(),'%y%m%d%H'),

date_format(lrrq,'%Y%m%d %H')>= date_format(date_sub(now(),interval 1 day),'%Y%m%d 00')
and date_format(lrrq,'%Y%m%d %H')<= date_format(date_sub(now(),interval 1 day),'%Y%m%d% 23')
)
union all
#当天全量App办理
select 'APP当天累计办理' as 类型，round(count(1) /10000,1) as 数量
from f_rt_SB_ZHSD_NDZXSB_ZB_qccx
where 
if(
date_format(now(),'%Y%m%d %H') != date_format(now(),'%Y%m%d 00'),

date_format(lrrq,'%y%m%d')>= date_format(now(),'%y%m%d')
 and date_format(lrrq,'%y%m%d%H')< date_format(now(),'%y%m%d%H')
 and jyqd_dm= '11'
 and(DLJGLX_DM is null
 or DLJGLX_DM= ''),

date_format(lrrq,'%Y%m%d %H')>= date_format(date_sub(now(),interval 1 day),'%Y%m%d 00')
 and date_format(lrrq,'%Y%m%d %H')<= date_format(date_sub(now(),interval 1 day),'%Y%m%d% 23')
 and jyqd_dm= '11'
 and(DLJGLX_DM is null
 or DLJGLX_DM= '')
 );"""
        cursor_ads.execute(sql1)
        ywbl=cursor_ads.fetchall()
        for i in ywbl:
            print(i)
    except Exception as f:
        print(f)
def main():
    dlrw()
    ywbl_app()
    db_gglog.close()
    db_ads.close()











