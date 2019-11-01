# -*- coding: utf-8 -*-
"""
@author: 东风
@file: 5.2-基本功能.py
@time: 2019/10/16 9:34
"""

from pprint import pprint
import pandas as pd
import numpy as np
from pandas import Series, DataFrame


# 5.2.1 重建索引
obj = pd.Series([4.5, 7.2, -5.3, 3.6])
print(obj)
print("重建索引")
obj = pd.Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
print(obj)

print("\n")
obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])
print(obj2)

print("\n")
obj3 = pd.Series(['bule', 'purple', 'yellow'], index=[0, 2, 4])
print(obj3)

print("\n")
print(obj3.reindex(range(6), method='ffill'))

print("\n")
frame = pd.DataFrame(np.arange(9).reshape((3, 3)), index=['a', 'c', 'd'], columns=['Ohio', 'Texas', 'California'])
print(frame)
frame2 = frame.reindex(['a', 'b', 'c', 'd'])
print(frame2)

print("\n")
states = ['Texas', 'Utah', 'California']
print(frame.reindex(columns=states))
"""
reindex方法的参数
index：新建作为索引的序列，可以是索引实例或任意其他序列型Python数据结构，索引使用时无需复制
"""

print("\n")
print(frame.loc[['a','b', 'c', 'd'], states])

# 5.2.2 轴向上删除目录
print("\n")
obj = pd.Series(np.arange(5.), index=['a', 'b', 'c', 'd', 'e'])
print(obj)
new_obj = obj.drop('c')
print(new_obj)
print(obj.drop(['d', 'c']))

print("\n")
data = pd.DataFrame(np.arange(16).reshape((4, 4)), index=['Ohio', 'Colorado', 'Utah', 'New York'], columns=['one', 'two', 'three', 'four'])
print(data)

print("\n")
print(data.drop(['Colorado', 'Ohio']))

print("\n")
print(data.drop('two', axis=1))

print("\n")
obj.drop('c', inplace=True)
print(obj)

# 5.2.3 索引、选择与过滤
print("\n")
obj = pd.Series(np.arange(4.), index=['a', 'b', 'c', 'd'])
print(obj)
print(obj['b'])
print(obj[1])
print(obj[2:4])
print(obj[['b', 'a', 'd']])
print(obj[[1, 3]])
print(obj[obj < 2])

print("\n")
print(obj['b': 'c'])
obj['b':'c'] = 5
print(obj)

print("\n")
data = pd.DataFrame(np.arange(16).reshape((4, 4)), index=['Ohio', 'Colorado', 'Utah', 'New York'], columns=['one', 'two', 'three', 'four'])
print(data)
print(data['two'])
print(data[['three', 'one']])
print(data[:2])
print(data[data['three'] > 5])

print("\n")
print(data < 5)
data[data < 5] = 0
print(data)

# 5.2.3.1 使用loc和iloc选择数据
print("\n")
print(data.loc['Colorado', ['two', 'three']])

print("\n")
print(data.iloc[2, [3, 0, 1]])
print(data.iloc[2])
print(data.iloc[[1, 2], [3, 0, 1]])

print("\n")
print(data.loc[:'Utah', 'two'])
print(data.iloc[:, :3][data.three > 5])

"""
DataFrame索引选项
df[val]：从DataFrame 		选取单列或一组列；在特殊情况下比较便利；布尔型数组(过滤)、切片（行切片）、或布尔型DataFrame（根据条件设置值）
df.loc[val]： 				通过标签，选取DataFrame的单个行或一组房
df.loc[;, val]： 			通过标签，选取单列或列子集
df.loc[val1, val2]： 		通过标签，同时选取行和列
df.iloc[where]： 			通过整数位置，从DataFrame选取单个行或行子集
df.iloc[;, where]： 			通过整数位置，从DataFrame选取单个列或列子集
df.iloc[where_i, where_j]： 通过整数位置，同时选取行和列
df.at[label_i, label_j]： 	通过行和列标签，选取单一的标量
df.iat[i, j]： 				通过行和列的位置（整数），选取单一的标量
reindex： 					通过标签选取行或列
get_value,set_value： 		通过行和列标签选取单一值

"""

# 5.2.4 整数索引
print("\n")
ser = pd.Series(np.arange(3.))
print(ser)
# print(ser[-1])

ser2 = pd.Series(np.arange(3.), index=['a', 'b', 'c'])
print(ser2)
print(ser2[-1])

print("\n")
print(ser[:1])
print(ser.loc[:1])
print(ser.iloc[:1])

# 5.2.5 算术和数据对齐
print("\n")
s1 = pd.Series([7.3, -2.5, 3.4, 1.5], index=['a', 'c', 'd', 'e'])
s2 = pd.Series([-2.1, 3.6, -1.5, 4, 3.1], index=['a', 'c', 'e', 'f', 'g'])
print(s1)
print(s2)
print(s1 + s2)

print("\n")
df1 = pd.DataFrame(np.arange(9.).reshape((3, 3)), columns=list('bcd'), index=['Ohio', 'Texas', 'Colorado'])
df2 = pd.DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'), index=['Utah', 'Ohio', 'Texas', 'Oregon'])
print(df1)
print(df2)
print(df1 + df2)

print("\n")
df1 = pd.DataFrame({'A': [1, 2]})
df2 = pd.DataFrame({'B': [3, 4]})
print(df1)
print(df2)
print(df1 - df2)

# 5.2.5.1 使用填充值的算术方法
print("\n")
df1 = pd.DataFrame(np.arange(12.).reshape((3, 4)), columns=list('abcd'))
df2 = pd.DataFrame(np.arange(20.).reshape((4, 5)), columns=list('abcde'))
df2.loc[1, 'b'] = np.nan
print(df1)
print(df2)
print(df1 + df2)
print(df1.add(df2, fill_value=0))
print(1 / df1 )
print(df1.rdiv(1))
print(df1.reindex(columns=df2.columns, fill_value=0))
"""
灵活的算术方法
add, radd：用于加法的方法
sub, rsub：用于减法的方法
div, rdiv：用于除法的方法
floordiv, rfloordiv：用于底除的方法
mul, rmul：用于乘法的方法
pow, rpow：用于指数的方法
"""

# 5.2.5.2 DataFrame和Series间的操作
print("\n")
arr = np.arange(12.).reshape((3, 4))
print(arr)
pprint(arr[0])
pprint(arr - arr[0])

print("\n")
frame = pd.DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'), index=['Utah', 'Ohio', 'Texas', 'Oregon'])

series = frame.iloc[0]
print(frame)
print(series)
print(frame - series)

print("\n")
series2 = pd.Series(range(3), index=['b', 'e', 'f'])
print(series2)
print(frame + series2)

print("\n")
series3 = frame['d']
print(series3)
print(frame)
print(frame.sub(series3, axis='index'))

# 5.2.6 函数应用和映射
print("\n")
frame = pd.DataFrame(np.random.randn(4, 3), columns=list('bde'), index=['Utah', 'Ohio', 'Texas', 'Oregon'])
print(frame)
print(np.abs(frame))

print("\n")
f = lambda x: x.max() - x.min()
print(frame.apply(f))
print(frame.apply(f, axis='columns'))

print("\n")
def f(x):
	return pd.Series([x.min(), x.max()], index=['min', 'max'])
print(frame)
print(frame.apply(f))

print("\n")
format = lambda x: '%.2f' % x
print(frame.applymap(format))

print("\n")
print(frame['e'].map(format))

# 5.2.7 排序和排名
print("\n")
obj = pd.Series(range(4), index=['d', 'a', 'b', 'c'])
print(obj)
print(obj.sort_index())

print("\n")
frame = pd.DataFrame(np.arange(8).reshape((2, 4)), index=['three', 'one'], columns=['d', 'a', 'b', 'c'])
print(frame)
print(frame.sort_index())
print(frame.sort_index(axis=1))

print("\n")
print(frame.sort_index(axis=1, ascending=False))

print("\n")
obj = pd.Series([4, 7, -3, 2])
print(obj.sort_values())

print("\n")
obj = pd.Series([4, np.nan, 7, np.nan, -3, 2])
print(obj.sort_values())

print("\n")
frame = pd.DataFrame({'b': [4, 7, -3, 2], 'a': [0, 1, 0, 1]})
print(frame)
print(frame.sort_values(by='b'))

print("\n")
print(frame.sort_values(by=['a', 'b']))

print("\n")
obj = pd.Series([7, -5, 7, 4, 2, 0, 4])
print(obj)
print(obj.rank())

print("\n")
print(obj.rank(method='first'))

print("\n")
print(obj.rank(ascending=False, method='max'))
"""
排名中的平级关系打破方法
average：默认；在相等分组中，为各个值分配平均排名
min：使用整个分组的最小排名
max：使用整个分组的最大排名
first：按值在原始数据中的出现顺序分配排名
dense：类似于‘min’方法，但是排名总是在组间加1，而不是组中相同的元素数
"""
print("\n")
frame = pd.DataFrame({'b': [4.3, 7, -3, 2], 'a': [0, 1, 0, 1], 'c': [-2, 5, 8, -2.5]})
print(frame)
print(frame.rank(axis='columns'))


# 5.2.8 含有重复标签的轴索引
print("\n")
obj = pd.Series(range(5), index=['a', 'a', 'b', 'b', 'c'])
print(obj)
print(obj.index.is_unique)

print("\n")
print(obj['a'])
print(obj['c'])

print("\n")
df = pd.DataFrame(np.random.randn(4, 3), index=['a', 'a', 'b', 'b'])
print(df)
print(df.loc['b'])
