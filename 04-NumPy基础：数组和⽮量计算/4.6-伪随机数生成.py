# -*- coding: utf-8 -*-
"""
@author: 东风
@file: 4.6-伪随机数生成.py
@time: 2019/10/12 17:39
"""

import numpy as np
from pprint import pprint

# normal获得4*4的正态分布样本数据
samples = np.random.normal(size=(4, 4))
pprint(samples)

"""
numpy.random在生成大型样本时比存Python的方式快了一个数量级
%timeit samples = [normalvariate(0, 1) for _ in range(N)]
1.61 s �� 88.6 ms per loop (mean �� std. dev. of 7 runs, 1 loop each)

%timeit np.random.normal(size=N)
42.2 ms �� 2.15 ms per loop (mean �� std. dev. of 7 runs, 10 loops each)
"""

"""
numpy.random中的部分函数列表
seed：向随机数生成器传递随机状态种子
permutation：返回一个序列的随机排列，或者返回一个乱序的整数范围序列
shuffle：随机排列一个序列
rand：从均匀分布中抽取样本
randint：根据跟定的由低到高的方位抽取随机整数
randn：从均值0方差1的正态分布中抽取样本
binomial：从二项分布中抽取样本
normal：从正态分布中抽取样本
beta：从beta分布中抽取样本
chisquare：从卡方分布中抽取样本
"""
