# -*- coding: utf-8 -*-
"""
@author: 东风
@file: 4.7-示例-随机漫步.py
@time: 2019/10/12 17:39
"""
import random
import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint


# 纯Python实现
# position = 0
# walk = [position]
# steps = 1000
# for i in range(steps):
#     step = 1 if random.randint(0, 1) else -1
#     position += step
#     walk.append(position)
# plt.plot(walk[:100])
# plt.show()

print("模拟1000次投掷硬币的结果，每次投掷的结果为1或-1，然后计算累积值")
# nsteps = 1000
# draws = np.random.randint(0, 2, size=nsteps)
# steps = np.where(draws > 0, 1, -1)
# walk = steps.cumsum()
# print(walk.min())
# print(walk.max())

print("\n一次模拟多次随机漫步")
nwalks = 5000
nsteps = 1000
draws = np.random.randint(0, 2, size=(nwalks, nsteps))
steps = np.where(draws > 0, 1, -1)
walks = steps.cumsum(1)
pprint(walks)

print("随机步的最大值和最小值")
print(walks.max())
print(walks.min())

print("计算歘30或-30的最小穿越时间")
hits30 = (np.abs(walks) >= 30).any(1)
print(hits30)
print(hits30.sum())

print("选出绝对步数超过30的步所在行")
crossing_times = (np.abs(walks[hits30]) >= 30).argmax(1)
print(crossing_times.mean())
