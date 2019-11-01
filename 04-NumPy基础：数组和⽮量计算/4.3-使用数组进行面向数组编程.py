# -*- coding: utf-8 -*-
"""
@author: 东风
@file: 4.3-使用数组进行面向数组编程.py
@time: 2019/10/12 17:38
"""

import numpy as np
from pprint import pprint
import matplotlib.pyplot as plt

# 向量化：利用数组表达式来替代显示循环的方法
# 示例
# points = np.arange(-5, 5, 0.01)
# pprint(points)

# meshgrid函数接收两个一维数组，并根据两个数字的所有(x,y)对生成一个二维矩阵
# xs, ys = np.meshgrid(points, points)
# pprint(ys)

# 可以用和两个坐标值同样的表达式来使用函数
# z = np.sqrt(xs ** 2 + ys ** 2)
# pprint(z)

# 使用matplotlib来生成二维数组的可视化
# plt.imshow(z, cmap=plt.cm.gray);
# plt.colorbar()
# plt.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid of values")
# plt.show()

# 4.3.1 将条件逻辑作为数组操作
# numpy.where函数是三元表达式x if condition else y的向量化版
xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])
# 需求：cond元素为True时，取xarr中对应元素，否则取yarr中的元素
result = [(x if c else y) for x, y, c in zip(xarr, yarr, cond)]
pprint(result)

# np.where第二个和第三个参数并不需要是数组，可以是标量
print("\n用np.where优化")
result = np.where(cond, xarr, yarr)
pprint(result)

print("\n利用where根据一个数组来生成一个新的数组")
arr = np.random.randn(4, 4)
pprint(arr)
pprint(arr > 0)
pprint(np.where(arr > 0, 2, -2))

print("\nnp.where将标量和数组联合")
print("传递给np.where的数组既可以是同等大小的数组，也可以是标量")
pprint(np.where(arr > 0, 2, arr)) # 仅将正值设为2


# 4.3.2 数学和统计方法
print("\n正态分布的随机数，计算部分聚合统计数据")
arr = np.random.randn(5, 4)
pprint(arr)
print(arr.mean())
pprint(np.mean(arr))
print(arr.sum())

print("\n通过参数axis，用于计算给定轴向上的统计值，形成一个下降一维度的数组")
pprint(arr.mean(axis=1)) # 表示“计算每一列的平均值”
pprint(arr.sum(axis=0)) # 表示“计算行轴向的累和”

print("\ncumsum和cumprod并不会聚合，会产生一个中间结果")
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7])
pprint(arr.cumsum())

print("\n部分聚合")
arr = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
pprint(arr)
pprint(arr.cumsum(axis=0))
pprint(arr.cumprod(axis=1))

"""
基础数组统计方法
sum：沿着轴向计算所有元素的累和，0长度的数组，累和为0
mean：数学平均，0长度的数组平均值为NaN
std，var：标准差和方差，可以选择自由度调整(默认分母是n)
min，max：最小值和最大值
argmin，argmax：最小值和最大值的位置
cumsum：从0开始元素累积和
cumprod：从1开始元素累积积
"""

# 4.3.3 布尔值数组的方法
print("\nsum可以用于计算布尔数组中的True的个数")
arr = np.random.randn(100)
# pprint(arr)
print((arr > 0).sum())

# 布尔数组方法
print("\nany检查数组中是否至少有一个True")
bools = np.array([False, False, True, False])
print(bools.any())
print("\nall检查是否每个值都是True")
print(bools.all())
# 这些方法也可适用于非布尔数组，所有的非0元素都会按True处理

# 4.3.4 排序
print("\nsort方法按位置排序")
arr = np.random.randn(6)
pprint(arr)
arr.sort()
pprint(arr)

print("\n在多维数组中根据传递的axis值，沿着轴向对每个一维数据进行排序")
arr = np.random.randn(5, 4)
pprint(arr)
arr.sort(1) # 返回的是已经排序好的数组拷贝，而不是对原数组按位置排序
pprint(arr)

print("\n计算数组的分位数，并选出分位数所对应的的值")
large_arr = np.random.randn(1000)
large_arr.sort()
print(large_arr[int(0.05 * len(large_arr))])


# 4.3.5 唯一值与其他集合逻辑
print("\nnp.unique，返回的是数组中唯一值排序后形成的数组")
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
pprint(np.unique(names))
ints = np.array([3, 3, 3, 2, 2, 1, 1, 4, 4])
pprint(np.unique(ints))

print("\nnp.unique和存Python实现相比较")
print(sorted(set(names)))

print("\nnpin1d,检查一个数组中的值是否在另外一个数组中，并返回一个布尔值数组")
values = np.array([6, 0, 0, 3, 2, 5, 6])
pprint(np.in1d(values, [2, 3, 6]))
"""
数组的集合操作
unique(x) 计算x的唯一值，并排序
intersect1d(x, y) 计算x和y的交集，并排序
union1d(x, y) 计算x和y的并集，并排序
in1d(x, y) 计算x中的元素是否包含在y中，返回一个布尔值数组
setdiff1d(x, y) 差集，在x中但不在y中的x的元素
setxor1d(x, y) 异或集，在x或y中，但不属于x，交集的元素
"""

