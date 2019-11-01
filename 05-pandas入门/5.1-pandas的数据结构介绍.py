# -*- coding: utf-8 -*-
"""
@author: 东风
@file: 5.1-pandas的数据结构介绍.py
@time: 2019/10/16 9:34
"""

from pprint import pprint
import pandas as pd
import numpy as np
from pandas import Series, DataFrame


# 5.1.1 Series
print("Series是一种一维的数组型对象，它包含了一个值序列（与NumPy中的类型相似），并包含了数据标签，称为索引")
obj = pd.Series([4, 7, -5, 3])
# pprint(obj)
print(obj)

print("\n通过values和index属性分别获得Series对象的值和索引")
print(obj.values)
print(obj.index)

print("\n创建一个索引序列，用标签标识每个数据点")
obj2 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
print(obj2)
print(obj2.index)

print("\n标量、数学函数应用")
print(obj2[obj2 > 0])
print(obj2 * 2)
print(np.exp(obj2))

# Series可以认为是一个长度固定且有序的字典
print('b' in obj2)
print('e' in obj2)


# 5.1.2 DataFrame

# 5.1.3 索引对象

