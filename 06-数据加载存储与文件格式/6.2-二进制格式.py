# -*- coding: utf-8 -*-
"""
@author: 东风
@file: 6.2-二进制格式.py
@time: 2019/10/22 11:23
"""

import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from pprint import pprint
import sys
import csv
import json

path = 'D:/data/pydata_book2/examples/ex1.csv'
# frame = pd.read_csv(path)
# pprint(frame)

# 写入二进制文件
# frame.to_pickle('D:/data/pydata_book2/examples/frame_pickle')

# 读取二进制文件
pprint(pd.read_pickle('D:/data/pydata_book2/examples/frame_pickle'))

# 6.2.1 使用HDF5格式
print("\nHDF5格式")
frame = pd.DataFrame({'a': np.random.randn(100)})
# pprint(frame)
store = pd.HDFStore('mydata.h5')
store['obj1'] = frame
store['obj1_col'] = frame['a']
# pprint(store)

print("\n进行索引")
# pprint(store['obj1'])

# print("\nHDFStore支持两种存储模式：'fixed'和'table'，否则速度更慢，但支持一种特殊语法的查询操作")
# store.put('obj2', frame, format='table')
# pprint(store.select('obj2', where=['index >= 10 and index <= 15']))

print("\npandas.read_hdf函数是这些工具的快捷方法")
# frame.to_hdf('mydata.h5', 'obj3', format='table')
# print(pd.read_hdf('mydata.h5', 'obj3', where=['index < 5']))


# 6.2.2 读取Microsoft Excel文件
print("\n读取Microsoft Excel文件")
# 生成一个实例
xlsx = pd.ExcelFile('D:/data/pydata_book2/examples/ex1.xlsx')
print("\n通过pandas.read_excel读取到DataFrame中")
pprint(pd.read_excel(xlsx, 'Sheet1'))

# 读取多个表的文件
frame = pd.read_excel('D:/data/pydata_book2/examples/ex1.xlsx', 'Sheet1')
pprint(frame)

print('\n将pandas数据写入到Excel中')
writer = pd.ExcelWriter('D:/data/pydata_book2/examples/ex2.xlsx')
frame.to_excel(writer, 'Sheet1')

# 或是直接传路径给to_excel
# frame.to_excel('D:/data/pydata_book2/examples/ex2.xlsx')

writer.save()