#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fangshuai
# date:2020/xx/xx
import pymysql

mydb = pymysql.connect(host='rm-bp1p689196a0p9vr2co.mysql.rds.aliyuncs.com',
                       user='fs_cs',
                       passwd='Admin@123',
                       database='fs_cs')


class creatrable():
    def __int__(self):
        pass

    def creat_t_qps(self):
        cursor = mydb.cursor()
        cursor.execute("DROP TABLE IF EXISTS t_qps")
        sql = """CREATE TABLE `t_qps` (
      `id` int(6) NOT NULL AUTO_INCREMENT COMMENT '服务主键ID',
      `app_name` varchar(255) DEFAULT NULL COMMENT 'app名称',
      `peak_time` datetime NOT NULL COMMENT '峰值时间',
      `qps` decimal(10,0) DEFAULT NULL COMMENT 'qps值',
      `lrrq` datetime NOT NULL COMMENT '录入时间(缺省时间为当前时间)',
       PRIMARY KEY (`id`)
       ###UNIQUE KEY (`app_name`) (约束这边不需要)
       )
       """
        cursor.execute(sql)

    def creat_t_gc(self):
        cursor = mydb.cursor()
        cursor.execute("DROP TABLE IF EXISTS t_gc")
        sql = """CREATE TABLE `t_gc` (
         `id` int(6) NOT NULL AUTO_INCREMENT COMMENT '服务主键ID',
         `app_name` varchar(255) DEFAULT NULL COMMENT '应用名称',
         `gc_time` datetime NOT NULL COMMENT '峰值时间',
         `youngGc` decimal(10,0) DEFAULT NULL COMMENT 'gc值',
         `lrrq` datetime NOT NULL COMMENT '录入时间(缺省时间为当前时间)',
          PRIMARY KEY (`id`)
          ###UNIQUE KEY (`app_name`) (约束这边不需要)
          )
          """
        cursor.execute(sql)

    def creat_t_app_info(self):
        cursor = mydb.cursor()
        cursor.execute("DROP TABLE IF EXISTS t_app_info")
        sql = """CREATE TABLE `t_app_info` (
          `id` int(6) NOT NULL AUTO_INCREMENT COMMENT '主键ID',
          `pid` varchar(255) DEFAULT NULL COMMENT 'pid',
          `app_name` varchar(255) DEFAULT NULL COMMENT '应用名称',
          `lrrq` datetime NOT NULL COMMENT '录入时间(缺省时间为当前时间)',
           PRIMARY KEY (`id`)
           )
           """
        cursor.execute(sql)

    def db_close(self):
        mydb.close()


if __name__ == '__main__':
    creatrable = creatrable()
    creatrable.creat_t_app_info()
    creatrable.creat_t_gc()
    creatrable.creat_t_qps()
    creatrable.db_close()
