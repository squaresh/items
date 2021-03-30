#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fangshuai
# date:2020/xx/xx
import pandas as pd

data = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
        "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
        "area": [8.516, 17.10, 3.286, 9.597, 1.221],
        "population": [200.4, 143.5, 1252, 1357, 52.98]}  ####设置data

frame = pd.DataFrame(data)  ###调用dataframe函数生产数据
print(frame)

print('------------------------------')

frame.index = ["BR", "RU", "IN", "CH", "SA"] ###定义索引
print(frame)

df=pd.read_csv("D:/pycharm/projects/learn/study/txt/pandas.csv")  ##导入文件
print(df.to_string(index=False)) #### 打印导出的文件 不加索引
