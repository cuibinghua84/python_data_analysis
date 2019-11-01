# -*- coding: utf-8 -*-
"""
@author: 东风
@file: babynames.py
@time: 2019/10/10 11:49
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# 使用pandas.read_csv将其加载到DataFrame中
# names1880 = pd.read_csv('D:/data/pydata_book2/datasets/babynames/yob1880.txt', names=['name', 'sex', 'births'])
# print(names1880)

# 按性别列出的出生总和作为当年的出生总数
# print(names1880.groupby('sex').births.sum())

# 将所有数据集中到一个DataFrame中，再添加一个年份字段（可使用pandas.concat）
years = range(1880, 2011)
pieces = []
columns = ['name', 'sex', 'births']
for year in years:
    path = 'D:/data/pydata_book2/datasets/babynames/yob%d.txt' % year
    # print(path)
    frame = pd.read_csv(path, names=columns)
    frame['year'] = year
    pieces.append(frame)

# 将所有内容粘接近一个DataFrame中
names = pd.concat(pieces, ignore_index=True)
# print(names)

# 现在可使用groupby或pivot_table开始聚合年份和性别数据
total_births = names.pivot_table('births', index='year', columns='sex', aggfunc=sum)
# print(total_births.tail())

# 绘制图表
# total_births.plot(title='Total births by sex and year')
# plt.show()

# 插入prop列，给出每个婴儿名字相对出生总数的比例
# 首先按年份和性别对数据进行分组，然后将新列添加到每个组中
def add_prop(group):
    group['prop'] = group.births / group.births.sum()
    return group
names = names.groupby(['year', 'sex']).apply(add_prop)
# print(names)

# 进行完整性检查
# print(names.groupby(['year', 'sex']).prop.sum())

# 每个性别/年份组合的前1000名。
def get_top1000(group):
    return group.sort_values(by='births', ascending=False)[:1000]
grouped = names.groupby(['year', 'sex'])
top1000 = grouped.apply(get_top1000)
# 删除组索引，不需要它
top1000.reset_index(inplace=True, drop=True)

# DIY方式实现
# pieces = []
# for year, group in names.groupby(['year', 'sex']):
#     pieces.append(group.sort_values(by='births', ascending=False)[:1000])
# top1000 = pd.concat(pieces, ignore_index=True)

# print(top1000)

# 分析名字趋势
# 将Top1000的名字分成男孩和女孩
boys = top1000[top1000.sex == 'M']
girls = top1000[top1000.sex == 'F']

# 按年份和名字形成出生总数的数据透视表
# total_births = top1000.pivot_table('births', index='year', columns='name', aggfunc=sum)
# total_births.info()
# 绘制少数名称的透视表
# subset = total_births[['John', 'Harry', 'Mary', 'Marilyn']]
# subset.plot(subplots=True, figsize=(12, 10), grid=False, title='Number of births per year')
# plt.show()

# 计算命名多样性的增加
# 按照年份和性别进行聚合和绘图
# table = top1000.pivot_table('prop', index='year', columns='sex', aggfunc=sum)
# table.plot(title='Sum of table1000.prop by year and sex', yticks=np.linspace(0, 1.2, 13), xticks=range(1880, 2020, 10))
# plt.show()

df = boys[boys.year == 2010]
# print(df)

prop_cumsum = df.sort_values(by='prop', ascending=False).prop.cumsum()
# print(prop_cumsum[:10])

# print(prop_cumsum.values.searchsorted(0.5))

df = boys[boys.year == 1990]
in1990 = df.sort_values(by='prop', ascending=False).prop.cumsum()
# print(in1990.values.searchsorted(0.5) + 1)

def get_quantile_count(group, q=0.5):
    group = group.sort_values(by='prop', ascending=False)
    return group.prop.cumsum().values.searchsorted(q) + 1
diversity = top1000.groupby(['year', 'sex']).apply(get_quantile_count)
diversity = diversity.unstack('sex')
# print(diversity.head())

# diversity.plot(title='Number of popular names is top 50%')
# plt.show()

# “最后一个字母”革命
# 从name列提取最后一个字母
get_last_letter = lambda  x: x[-1]
last_tetters = names.name.map(get_last_letter)
last_tetters.name = 'last_letter'
table = names.pivot_table('births', index=last_tetters, columns=['sex', 'year'], aggfunc=sum)
subtable = table.reindex(columns=[1910, 1960, 2010], level='year')
# print(subtable)
# print(subtable.sum())

letter_prop = subtable / subtable.sum()
# print(letter_prop)

# fig, axes = plt.subplots(2, 1, figsize=(10, 8))
# letter_prop['M'].plot(kind='bar', rot=0, ax=axes[0], title='Male')
# letter_prop['F'].plot(kind='bar', rot=0, ax=axes[1], title='Female', legend=False)
# plt.show()

# letter_prop = table / table.sum()
# dny_ts = letter_prop.loc[['d', 'n', 'y'], 'M'].T
# print(dny_ts.head())
# dny_ts.plot()

# 男孩名字变成女孩名字
all_names = pd.Series(top1000.name.unique())
lesley_like = all_names[all_names.str.lower().str.contains('lesl')]
# print(lesley_like)

filtered = top1000[top1000.name.isin(lesley_like)]
filtered.groupby('name').births.sum()

table = filtered.pivot_table('births', index='year', columns='sex', aggfunc='sum')
table = table.div(table.sum(1), axis=0)
print(table.tail())

table.plot(style={'M': 'k-', 'F': 'k--'})
plt.show()

