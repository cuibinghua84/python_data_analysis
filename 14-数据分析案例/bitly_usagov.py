# -*- coding: utf-8 -*-
# 导入库文件
# json将JSON字符串转换为Python字典对象
import json
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from pprint import pprint
from collections import defaultdict
from collections import Counter

path = 'D:/data/pydata_book2/datasets/bitly_usagov/example.txt'
# print(open(path).readline())

# 将json字符串转换为字典对象
records = [json.loads(line) for line in open(path)]
# pprint(records[0])

# 纯Python时区计数
time_zones = [rec['tz'] for rec in records if 'tz' in rec]


# pprint(time_zones[:10])

# 使用纯Python标准库遍历时区，使用字典来存储计数
def get_counts(sequence):
    counts = {}
    for x in sequence:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    return counts


# 使用Python标准库中的高级工具 defaultdict
def get_counts2(sequence):
    counts = defaultdict(int)  # 值将初始化为0
    for x in sequence:
        counts[x] += 1
    return counts


# 查看时区只需传入time_zones
counts = get_counts2(time_zones)


# pprint(counts['America/New_York'])
# pprint(len(time_zones))

# 统计前十的时区和它们的计数
def top_counts(count_dict, n=10):
    value_key_pairs = [(count, tz) for tz, count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:]


# pprint(top_counts(counts))

# 使用Counter类统计时区
# counts = Counter(time_zones)
# pprint(counts.most_common(10))

# 使用pandas进行时区计数
# 将记录的列表传递给pandas.DataFrame，生成DataFrame
frame = pd.DataFrame(records)
# pprint(frame.info())
# pprint(frame['tz'][:10])

# 使用value_counts方法统计series
tz_counts = frame['tz'].value_counts()
# pprint(tz_counts[:10])

# fillna方法替换缺失值，并为空字符串使用布尔数组索引
clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz == ''] = 'Unknown'
tz_counts = clean_tz.value_counts()
# print(tz_counts[:10])

# 使用seaborn包绘制水平柱状图
# subset = tz_counts[:10]
# sns.barplot(y=subset.index, x=subset.values)
# plt.show()

# a列包含了执行网址缩短的浏览器、设备或引用的信息
# pprint(frame['a'][1])
# pprint(frame['a'][50])
# pprint(frame['a'][51][:50])

# 分离字符串中的第一个标记，并对用户行为进行另一个概括
results = pd.Series([x.split()[0] for x in frame.a.dropna()])
# pprint(results[:5])

# pprint(results.value_counts()[:8])

# 将时区记录分解为windows和非windows用户
# 从数据中排除代理字符串
cframe = frame[frame.a.notnull()]
# 拷贝
cframe = cframe.copy()
# 计算一个代表每一行是否是windows的值
# cframe['os'] = np.where(cframe['a'].str.contains('Windows'), 'Windows', 'Not Windows')
cframe['os'] = np.where(cframe['a'].str.contains('Windows'), 'Windows', 'Not Windows')
# pprint(cframe['os'][:5])

# 根据时区列以及新生成的操作系统列对数据进行分组
by_tz_os = cframe.groupby(['tz', 'os'])

# 使用size进行分组计数，使用unstack对计算结果进行重塑
agg_counts = by_tz_os.size().unstack().fillna(0)
# pprint(agg_counts[:10])

# 选出总体计数最高的时区
# 用于升序排列
indexer = agg_counts.sum(1).argsort()
# pprint(indexer[:10])

# 使用take方法按顺序选出行，再对最后10行进行切片
count_subset = agg_counts.take(indexer[-10:])
# print(count_subset)

# pandas的nlargest方法同样可以实现
# print(agg_counts.sum(1).nlargest(10))

# 绘制一个堆积条形图
# 对绘图数据进行重新排列
count_subset = count_subset.stack()
count_subset.name = 'total'
count_subset = count_subset.reset_index()


# print(count_subset[:10])

# 进行绘图
# sns.barplot(x='total', y='tz', hue='os', data=count_subset)

# 将组百分比归一化为1
def norm_total(group):
    group['normed_total'] = group.total / group.total.sum()
    return group


results = count_subset.groupby('tz').apply(norm_total)
# sns.barplot(x='normed_total', y='tz', hue='os', data=results)

# 通过transform方法和groupby方法更有效地计算归一化之和
g = count_subset.groupby('tz')
results2 = count_subset.total / g.total.transform('sum')
