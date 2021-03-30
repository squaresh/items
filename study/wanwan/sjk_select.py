import mysql.connector
mydb= mysql.connector.connect(host="rm-bp1p689196a0p9vr2co.mysql.rds.aliyuncs.com",
                              user="csb_gnhj",
                              passwd="Servyou2019",
                              database="csb_gnhj")
data1=mydb.cursor() ##指定链接的数据库(获取操作游标)
sql="select * from %s"
avl=[('csb_aliyun_cn_hangzhou_kjtweb_service_info')]
data1.execute(sql,avl)  ###需要执行sql的语句---executemany批量执行数据
data=data1.fetchall() ## 捞取sql 返回数据以列表的形式
#### mydb.commit() 更新数据库 dml(updata,insert delete)语句需要用到   注意 ddl(create table drop table alter table truncate table)语句不需要应为她已经默认含有commit了所以回滚也没用
print(data)
for i in data:
    with open('data',mode='a+') as f:
        f.write(str(i)+'\n')
mydb.close()  ###关闭数据库
########mysql 操作需要 四部 首要条件链接信息搞对，1.cursor()指定哪个数据库操作2.要执行什么操作例如（execute查询）
        #####3.fetchall 捞取执行操作后的返回值(针对select操作)  4.close关闭数据库链接