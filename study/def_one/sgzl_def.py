#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fangshuai
# date:2020/xx/xx
sgzl1=r"""select concat('(\'',GROUP_CONCAT(PRD_UID SEPARATOR '\',\''),'\')') 
from ProcDefinition where PRD_FLAG='0' AND PRD_SWSX= 'SXA012041001'
and LENGTH(PRD_UID)<30 """
drcj_as="""select
concat(left(PRI_Reserved7, 3), '00000000') as SJ_SWJG,
count(PRI_ID) as start_count
from ProcInstance
where date_format(PRI_STARTTIME, '%Y-%m-%d') = date_format(now(), '%Y-%m-%d')
and left(PRI_Reserved7, 5) not in ('12102','22102','13302','23302','13502','23502','13702','23702','14403','24403')
group by SJ_SWJG

union all

select
concat(left(PRI_Reserved7, 5), '000000') as SJ_SWJG,
count(PRI_ID) as start_count
from ProcInstance
where date_format(PRI_STARTTIME, '%Y-%m-%d') = date_format(now(), '%Y-%m-%d')
and left(PRI_Reserved7, 5) in ('12102','22102','13302','23302','13502','23502','13702','23702','14403','24403')
group by SJ_SWJG
"""
drcj_asw="""select
PRI_Reserved8 as SWSX,
count(PRI_ID) as start_count
from ProcInstance
where date_format(PRI_STARTTIME, '%Y-%m-%d') = date_format(now(), '%Y-%m-%d')
and left(PRI_Reserved7, 5) not in ('12102','22102','13302','23302','13502','23502','13702','23702','14403','24403')
group by SWSX

union all

select
PRI_Reserved8 as SWSX,
count(PRI_ID) as start_count
from ProcInstance
where date_format(PRI_STARTTIME, '%Y-%m-%d') = date_format(now(), '%Y-%m-%d')
and left(PRI_Reserved7, 5) in ('12102','22102','13302','23302','13502','23502','13702','23702','14403','24403')
group by SWSX
"""
drjs_as="""select
concat(left(PRI_Reserved7, 3), '00000000') as SJ_SWJG,
count(PRI_ID) as end_count
from ProcInstance
where date_format(PRI_ENDTIME , '%Y-%m-%d') = date_format(now(), '%Y-%m-%d')
and left(PRI_Reserved7, 5) not in ('12102','22102','13302','23302','13502','23502','13702','23702','14403','24403')
group by SJ_SWJG

union all

select
concat(left(PRI_Reserved7, 5), '000000') as SJ_SWJG,
count(PRI_ID) as end_count
from ProcInstance
where date_format(PRI_ENDTIME , '%Y-%m-%d') = date_format(now(), '%Y-%m-%d')
and left(PRI_Reserved7, 5) in ('12102','22102','13302','23302','13502','23502','13702','23702','14403','24403')
group by SJ_SWJG
"""
drjs_asw="""select
PRI_Reserved8 as SWSX,
count(PRI_ID) as end_count
from ProcInstance
where date_format(PRI_ENDTIME , '%Y-%m-%d') = date_format(now(), '%Y-%m-%d')
and left(PRI_Reserved7, 5) not in ('12102','22102','13302','23302','13502','23502','13702','23702','14403','24403')
group by SWSX

union all

select
PRI_Reserved8 as SWSX,
count(PRI_ID) as end_count
from ProcInstance
where date_format(PRI_ENDTIME , '%Y-%m-%d') = date_format(now(), '%Y-%m-%d')
and left(PRI_Reserved7, 5) in ('12102','22102','13302','23302','13502','23502','13702','23702','14403','24403')
group by SWSX
"""
hzzx_as="""select
concat(left(PRI_Reserved7, 3), '00000000') as SJ_SWJG,
count(PRI_ID) as runing_count
from ProcInstance
where PRI_STATE = 1
and left(PRI_Reserved7, 5) not in ('12102','22102','13302','23302','13502','23502','13702','23702','14403','24403')
group by
SJ_SWJG

union all

select
concat(left(PRI_Reserved7, 5), '000000') as SJ_SWJG,
count(PRI_ID) as runing_count
from ProcInstance
where PRI_STATE = 1
and left(PRI_Reserved7, 5) in ('12102','22102','13302','23302','13502','23502','13702','23702','14403','24403')
group by
SJ_SWJG"""
hzzs_asw="""select
PRI_Reserved8 as SWSX,
count(PRI_ID) as runing_count
from ProcInstance
where PRI_STATE = 1
and left(PRI_Reserved7, 5) not in ('12102','22102','13302','23302','13502','23502','13702','23702','14403','24403')
group by SWSX

union all

select
PRI_Reserved8 as SWSX,
count(PRI_ID) as runing_count
from
ProcInstance
where PRI_STATE = 1
and left(PRI_Reserved7, 5) in ('12102','22102','13302','23302','13502','23502','13702','23702','14403','24403')
group by SWSX
"""