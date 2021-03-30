#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fangshuai
# date:2020/xx/xx
from matplotlib import pyplot as plt
from matplotlib import style

style.use('ggplot')  ###套用这个模块的主题颜色

x = [3, 2, 4, 1,5]  ##定义x轴的位置 1表示第一个 2表示第二排序 (定义x轴的数字的数量)(最小表示第一个 以此排序)
y = [46, 1, 29, 22, 13]   ##设置y轴  上下对应写入 对应识别

fxg,ax = plt.subplots() ###固定语法 函数返回图像和轴对象

ax.bar(x, y, align='center') ###使用bar()功能生成条形图

ax.set_title('Olympic Gold medals in London')  ####设置主题
ax.set_ylabel('Gold medals')   ###设置轴的名称
ax.set_xlabel('Countries')   ###设置x周的名称

ax.set_xticks(x) ###给x轴付别名的函数
ax.set_xticklabels(("USA", "China", "UK", "Russia",
    "South Korea"))   #### 和x轴对应名称 对应识别

plt.show()  ###展示图片