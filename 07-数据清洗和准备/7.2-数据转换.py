# -*- coding: utf-8 -*-
"""
@author: 东风
@file: 7.2-数据转换.py
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

# 7.2.1 删除重复值
data = pd.DataFrame({'k1': ['one', 'two'] * 3 + ['two'], 'k2': [1, 1, 2, 3, 3, 4, 4]})
print(data)

print()
print(data.duplicated())

print()
print(data.drop_duplicates())

print()
data['v1'] = range(7)
print(data)
print(data.drop_duplicates(['k1']))

print()
print(data.drop_duplicates(['k1', 'k2'], keep='last'))


# 7.2.2 使用函数或映射进行数据转换
print()
data = pd.DataFrame({'food': ['bacon', 'pulled pork', 'bacon', 'Pastrami', 'corned beef', 'Bacon', 'pastrami', 'honey ham', 'nova lox'],
					 'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})
print(data)
meat_to_animal = {
	'bacon': 'pig',
	'pulled pork': 'pig',
	'pastrami': 'cow',
	'corned beef': 'cow',
	'honey ham': 'pig',
	'nova lox': 'salmon'
}
print()
lowercased = data['food'].str.lower()
print(lowercased)
data['animal'] = lowercased.map(meat_to_animal)
print(data)

print()
print(data['food'].map(lambda x: meat_to_animal[x.lower()]))

# 7.2.3 替代值
print()
data = pd.Series([1., -999., 2., -999., -1000., 3.])
print(data)
print(data.replace(-999, np.nan))

print()
print(data.replace([-999, -1000], np.nan))

print()
print(data.replace([-999, -1000], [np.nan, 0]))

print()
print(data.replace({-999: np.nan, -1000: 0}))

# 7.2.4 重命名轴索引
print()
data = pd.DataFrame(np.arange(12).reshape((3, 4)), index=['Ohio', 'Colorado', 'New York'], columns=['one', 'two', 'three', 'four'])
transform = lambda x: x[:4].upper()
# data.index.map(tran)
print()
print()
print()
print()
print()
print()
# 7.2.5 离散化和分箱

# 7.2.6 检测和过滤异常值

# 7.2.7 置换和随机抽样

# 7.2.8 计算指标/虚拟变量