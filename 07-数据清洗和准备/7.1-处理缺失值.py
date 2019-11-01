# -*- coding: utf-8 -*-
"""
@author: 东风
@file: 7.1-处理缺失值.py
@time: 2019/10/25 17:35
"""

import numpy as np
from numpy import nan as NA
import pandas as pd
from pandas import Series, DataFrame
from pprint import pprint
import sys
import csv
import json

print("pandas使用浮点值NaN")
string_data = pd.Series(['aardvark', 'artichoke', np.nan, 'avocado'])
pprint(string_data)
pprint(string_data.isnull())

print("\nPython内建的None值在对象数组中也被当做NA处理")
string_data[0] = None
print(string_data)
print(string_data.isnull())

"""NA处理方法
dropna	根据每个标签的值是否是缺失数据来刷选轴标签，并根据允许丢失的数据量来确定阀值
fillna	用某些值填充缺失的数据或使用插值方法(如'ffill'或'bfill')
isnull	返回表明哪些值是缺失值的布尔值
notnull isnull的反函数"""

# 7.1.1 过滤缺失值
print("\ndropna过滤缺失值")
data = pd.Series([1, NA, 3.5, NA, 7])
print(data.dropna())
print(data[data.notnull()])

print("\n处理DataFrame对象")
data = pd.DataFrame([[1., 6.5, 3.], [1., NA, NA], [NA, NA, NA], [NA, 6.5, 3.]])
pprint(data)
cleaned = data.dropna()
pprint(data)

print("\n传入how='all'，删除所有值均为NA的行")
print(data.dropna(how='all'))

print("\naxis=1 删除所有值为NA的列")
data[4] = NA
print(data.dropna(axis=1, how='all'))

print("\n保留包含一定数量的观察值的行，用thresh参数")
df = pd.DataFrame(np.random.randn(7, 3))
print(df)
df.iloc[:4, 1] = NA
df.iloc[:2, 2] = NA
print(df)
print(df.dropna())
print(df.dropna(thresh=2))

# 7.1.2 补全缺失值
print("\n补全缺失值：fillna方法补全缺失值")
print(df.fillna(0))

print("\n设定不同的填充值")
print(df.fillna({1: 0.5, 2: 1}))

print("\nfillna返回的是一个新对象，也可以修改已经存在的对象")
_ = df.fillna(0, inplace=True)
print(df)

print("\n重建索引的相同的插值方法也可以用于fillna")
df = pd.DataFrame(np.random.randn(6, 3))
df.iloc[2:, 1] = NA
df.iloc[4:, 2] = NA
print(df)
print(df.fillna(method='ffill'))
print(df.fillna(method='ffill', limit=2))

print("\n将Series的平均值或中位数用于填充缺失值")
data = pd.Series([1., NA, 3.5, NA, 7])
print(data.fillna(data.mean()))

"""
fillna函数参数
value 	标量值或字典型对象用于填充缺失值
method 	插值方法，如果没有其他参数，默认是'ffill'
axis 	需要填充的轴，默认是axis=0
inplace 修改被调用的对象，而不是生成一个备份
limit 	用于向前或向后填充时最大的填充范围"""
