#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fangshuai
# date:2020/xx/xx
import matplotlib.pyplot as plt   ###matplotlib 画图模块

labels = ['Oranges', 'Pears', 'Plums', 'Blueberries']  ##定义标签
quantity = [38, 45, 24, 10]   ##定义权重

colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']  ###定义颜色

plt.pie(quantity, labels=labels, colors=colors, autopct='%1.1f%%',   #####调用饼状涂模块 并且对应属性写上
    shadow=True, startangle=90)

plt.axis('equal') ###设置相同床宽比

plt.show()   ###展示