# -*- coding: utf-8 -*-
"""
@author: 东风
@file: 5.3-汇总和计算描述统计.py
@time: 2019/10/16 9:34
"""

import numpy as np
import pandas as pd
from pprint import pprint
from pandas import Series, DataFrame
import pandas_datareader.data as web

print("")
df = pd.DataFrame([[1.4, np.nan], [7.1, -4.5], [np.nan, np.nan], [0.75, -1.3]], index=['a', 'b', 'c', 'd'], columns=['one', 'two'])
print(df)
print(df.sum())

print("\n")
print(df.sum(axis='columns'))

print("\n")
print(df.mean(axis='columns', skipna=False))
"""
归纳方法可选参数
axis： 		约简的轴。DataFrame的行用0，列用1
skipna：		排除缺失值，默认值为True
level：		如何轴是层次化索引的，则根据level汉族约检
"""

print("\n")
print(df)
print(df.idxmax())
print(df.cumsum())

print("\n")
print(df.describe())

print("\n")
obj = pd.Series(['a', 'a', 'b', 'c'] * 4)
print(obj)
print(obj.describe())

"""
count			非NA值的个数
describe 		计算Series或DataFrame各列的汇总统计集合
min,max 		计算最小值 最大值
argmin, argmax 	分别计算最小值 最大值所在的索引位置(整数)
idxmin, idxmax 	分别计算最小值或最大值所在的索引标签
quantile 		计算样本的从0到1间的分位数
sum 			加和
mean 			均值
median			中位数
mad 			平均值的平均绝对偏差
prod 			所有值的积
var 			值的样本方差
std 			值的样本标准差
skew 			样本偏度值（第三时刻）
kurt 			样本偏度值（第四时刻）
cumsum 			累积值
cummin, cummax 	累积值的最小值或最大值
cumprod 		值的累积值
diff 			计算第一个算术差值（对时间序列有用）
pct_change 		计算百分比
"""

# 5.3.1 相关性和协方差
# print("\n")
# all_data = {ticker: web.get_data_yahoo(ticker) for ticker in ['AAPL', 'IBM', 'MSFT', 'GooG']}
# price = pd.DataFrame({ticker: data['Adj Close'] for ticker, data in all_data.items()})
# volume = pd.DataFrame({ticker: data['Volume'] for ticker, data in all_data.items()})
# returns = price.pct_change()
# print(returns.tail())

# print("\n")
# print(returns['MSFT'].corr(returns['IBM']))
# print(returns['MSFT'].cov(returns['IBM']))
# print(returns.MSFT.corr(returns.IBM))

# print("\n")
# print(returns.corrwith(returns.IBM))
# print(returns.corrwith(volume))

# 5.3.2 唯一值、计数和成员属性
print("\n")
obj = pd.Series(['c', 'a', 'd', 'a', 'a', 'b', 'b', 'c', 'c'])
uniques = obj.unique()
pprint(uniques)
pprint(obj.value_counts())

print("\n")
pprint(pd.value_counts(obj.values, sort=False))

print("\n")
pprint(obj)
mask = obj.isin(['b', 'c'])
pprint(mask)
pprint(obj[mask])

print("\n")
to_match = pd.Series(['c', 'a', 'b', 'b', 'c', 'a'])
unique_vals = pd.Series(['c', 'b', 'a'])
pprint(pd.Index(unique_vals).get_indexer(to_match))
"""
唯一值、计数和集合成员属性方法
isin：计算表征Series中每个值是否包含于传入序列的布尔值数组
match：计算数组中每个值的整数索引，形成一个唯一值数组。有助于数据对齐和join类型的操作
unique：计算Series值中的唯一值数组，按照观察顺序返回
value_counts：返回一个Series，索引是唯一值序列，值是计数个数，按照个数降序排序
"""

print("\n")
data = pd.DataFrame({'Qu1': [1, 3, 4, 3, 4], 'Qu2': [2, 3, 1, 2, 3], 'Qu3': [1, 5, 2, 4, 4]})
print(data)

print("\n")
result = data.apply(pd.value_counts).fillna(0)
print(result)

print("\n")

print("\n")

print("\n")