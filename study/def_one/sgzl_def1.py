#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fangshuai
# date:2020/xx/xx
sgzl1=r"""select concat('(\'',GROUP_CONCAT(PRD_UID SEPARATOR '\',\''),'\')') 
from ProcDefinition where PRD_FLAG='0' AND PRD_SWSX= 'SXA012041001'
and LENGTH(PRD_UID)<30 """
sgzl_aswjg="""select
    SJ_SWJG '省级机关代码',
    sum(start_count) as '当日创建的流程数量',
    sum(end_count) as '当日结束的流程数量',
    sum(runing_count) as '还在执行中的流程数量'
from
    (
    select
        concat(left(PRI_Reserved7, 3), '00000000') as SJ_SWJG,
        count(PRI_ID) as start_count,
        0 as end_count,
        0 as runing_count
    from
        ProcInstance
    where
        date_format(PRI_STARTTIME, '%Y-%m-%d') = date_format(now(), '%Y-%m-%d')
        and left(PRI_Reserved7, 5) not in ('12102','22102','13302','23302','13502','23502','13702','23702','14403','24403')
    group by
        SJ_SWJG
union all
    select
        concat(left(PRI_Reserved7, 5), '000000') as SJ_SWJG,
        count(PRI_ID) as start_count,
        0 as end_count,
        0 as runing_count
    from
        ProcInstance
    where
        date_format(PRI_STARTTIME, '%Y-%m-%d') = date_format(now(), '%Y-%m-%d')
        and left(PRI_Reserved7, 5) in ('12102','22102','13302','23302','13502','23502','13702','23702','14403','24403')
    group by
        SJ_SWJG
union all
    select
        concat(left(PRI_Reserved7, 3), '00000000') as SJ_SWJG,
        0 as start_count,
        count(PRI_ID) as end_count,
        0 as runing_count
    from
        ProcInstance
    where
        date_format(PRI_ENDTIME , '%Y-%m-%d') = date_format(now(), '%Y-%m-%d')
        and left(PRI_Reserved7, 5) not in ('12102','22102','13302','23302','13502','23502','13702','23702','14403','24403')
    group by
        SJ_SWJG
union all
    select
        concat(left(PRI_Reserved7, 5), '000000') as SJ_SWJG,
        0 as start_count,
        count(PRI_ID) as end_count,
        0 as runing_count
    from
        ProcInstance
    where
        date_format(PRI_ENDTIME , '%Y-%m-%d') = date_format(now(), '%Y-%m-%d')
        and left(PRI_Reserved7, 5) in ('12102','22102','13302','23302','13502','23502','13702','23702','14403','24403')
    group by
        SJ_SWJG
union all
    select
        concat(left(PRI_Reserved7, 3), '00000000') as SJ_SWJG,
        0 as start_count,
        0 as end_count,
        count(PRI_ID) as runing_count
    from
        ProcInstance
    where
        PRI_STATE = 1
        and left(PRI_Reserved7, 5) not in ('12102','22102','13302','23302','13502','23502','13702','23702','14403','24403')
    group by
        SJ_SWJG
union all
    select
        concat(left(PRI_Reserved7, 5), '000000') as SJ_SWJG,
        0 as start_count,
        0 as end_count,
        count(PRI_ID) as runing_count
    from
        ProcInstance
    where
        PRI_STATE = 1
        and left(PRI_Reserved7, 5) in ('12102','22102','13302','23302','13502','23502','13702','23702','14403','24403')
    group by
        SJ_SWJG)
group by
    SJ_SWJG;
"""
sgzl_aswsx="""select
        pc.SWSX '税务事项代码',
        sum(pc.start_count) as '当日创建的流程数量',
        sum(pc.end_count) as '当日结束的流程数量',
        sum(pc.runing_count) as '还在执行中的流程数量'
from
        (
        select
                PRI_Reserved8 as SWSX,
                count(PRI_ID) as start_count,
                0 as end_count,
                0 as runing_count
        from
                ProcInstance
        where
                date_format(PRI_STARTTIME, '%Y-%m-%d') = date_format(now(), '%Y-%m-%d')
        group by
                SWSX
union all
        select
                PRI_Reserved8 as SWSX,
                0 as start_count,
                count(PRI_ID) as end_count,
                0 as runing_count
        from
                ProcInstance
        where
                date_format(PRI_ENDTIME , '%Y-%m-%d') = date_format(now(), '%Y-%m-%d')
        group by
                SWSX
union all
        select
                PRI_Reserved8 as SWSX,
                0 as start_count,
                0 as end_count,
                count(PRI_ID) as runing_count
        from
                ProcInstance
        where
                PRI_STATE = 1
        group by
                SWSX ) pc,
        wf_biz_type t
where
        pc.SWSX = t.BIZ_TYPE_ID
group by
        pc.SWSX;"""