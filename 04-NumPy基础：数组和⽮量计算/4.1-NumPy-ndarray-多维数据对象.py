# -*- coding: utf-8 -*-
"""
@author: 东风
@file: 4.1-NumPy-ndarray-多维数据对象.py
@time: 2019/10/11 23:03
"""
import numpy as np
from pprint import pprint

"""
Numpy的核心特征之一就是N-维数组对象——ndarray
ndarray是Python中一个快速、灵活的大型数据集容器
数据允许你使用类似标量的操作语法在整块数据上进行数学计算
"""
# 感受NumPy如何进行批量计算
# 生成随机数组
data = np.random.rand(2, 3)
pprint(data)
pprint(data * 10)
pprint(data + data)

# ndarray是一个通用的多维同类数据容器，即它包含的每一个元素均为相同类型；
# 每一个数组都有一个shape属性，用来表征数组每一维度的数量
# 每一个数组都有一个dtype属性，用来描述数组的数据类型
print(data.shape)
print(data.dtype)

# 4.1.1 生成ndarray
# 1 使用array函数：可接受任意的序列型对象
# 如列表转换
data1 = [6, 7.5, 8, 0, 1]
arr1 = np.array(data1)
pprint(arr1)
# 嵌套序列，如等长度的列表，将会自动转换成多维数组
data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr2 = np.array(data2)
pprint(arr2)
# 通过ndim和shape属性来确定是否为二维数组
pprint(arr2.ndim)
pprint(arr2.shape)
pprint(arr2.dtype)
# 2 zeros可以一次性创造全是0数组
pprint(np.zeros(10))
pprint(np.zeros((3, 6)))
# 3 ones可以一次性创造全是1数组
pprint(np.ones(10))
# 4 empty则可以创建一个没有初始化值的数组
pprint(np.empty((2, 3, 2)))

# arange是Python内建函数的数组版
pprint(np.arange(15))

"""
以下是标注数组的生成函数
如没有特殊指明，NumPy默认的数据类型是float64（NumPy专注于数值计算）
array：将输入数据转换为ndarray
asarray：将输入转化为ndarray，但如果输入是ndarray则不再复制
arange：Python内建函数range的数组版，返回一个数组
"""

# 4.1.2 ndarray的数据类型
# dtype：是一种特殊的对象，它包含了ndarray需要为某一种类型数据所申明的内存块信息
arr1 = np.array([1, 2, 3], dtype=np.float64)
arr2 = np.array([1, 2, 3], dtype=np.int32)
pprint(arr1.dtype)
pprint(arr2.dtype)

"""
NumPy数据类型列表

"""

# 可以使用astype方法显式地转换数组的数据类型
arr = np.array([1, 2, 3, 4, 5])
pprint(arr.dtype)
float_arr = arr.astype(np.float64)
print(float_arr.dtype)

# 浮点数转换成整数，小数点后的部分将被消除
arr = np.array([3.7, -1.2, -2.6, 0.5, 12.9, 10.1])
pprint(arr)
pprint(arr.astype(np.int32))

# 如果数组里面的元素都是表达数字含义的字符串，可通过astype转为数字
numeric_strings = np.array(['1.25', '-9.6', '42'], dtype=np.string_)
pprint(numeric_strings.astype(float))

# NumPy可以使用相同别名来表征与Python精度相同的Python数据类型；也可以使用dtype属性
# 使用astype时总是生成一个新的数组，即使你传入的dtype与之前一样
int_array = np.arange(10)
calibers = np.array([.22, .270, .35, .380, .44, .50], dtype=np.float64)
pprint(int_array.astype(calibers.dtype))
# 也可使用类型代码传入数据类型
empty_uint32 = np.empty(8, dtype='u4')
pprint(empty_uint32)

# 4.1.3 NumPy数组算术
arr = np.array([[1., 2., 3.], [4., 5., 6.]])
pprint(arr)
pprint(arr * arr)
pprint(arr - arr)

print("\n带有标量计算的算术操作，会把计算参数传递给数组的每一个元素")
pprint(1 / arr)
print("\n同尺寸数组之间的比较，会产生一个布尔值数组；不同尺寸的数组间的操作，将会用到广播特性")
arr2 = np.array([[0., 4., 1.], [7., 2., 12.]])
pprint(arr2)
pprint(arr2 > arr)

# 4.1.4 基础索引与切片
print("\n基础索引与切片")
arr = np.arange(10)
pprint(arr)
print(arr[5])
print(arr[5:8])
arr[5:8] = 12
pprint(arr)
# 区别于Python的内建列表，数组的切片是原数组的视图，数据并不是被复制了，任何对于视图的修改都会反映到原数组上
# 如果需要复制数组：就必须显式地复制 .copy()
arr_slice = arr[5:8]
pprint(arr_slice)
arr_slice[1] = 12345
pprint(arr)
# [:]=>将会引用数组的所有值
arr_slice[:] = 64
pprint(arr)

print("\n多维数组中，每个索引值对应的元素不再是一个值，而是一个一维数组")
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
pprint(arr2d)
pprint(arr2d[2])
print("\n获取单个元素")
print(arr2d[0][2])
print(arr2d[0, 2])
print("\n多维数组中，省略后面索引值，返回的对象是降低一个维度的数组")
arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
pprint(arr3d)
pprint(arr3d[0])
print("\n标量和数组都可以传递给arr3d[0]")
old_value = arr3d[0].copy()
pprint(old_value)
arr3d[0] = 42
pprint(arr3d)
arr3d[0] = old_value
pprint(arr3d)
print("\narr3d[1, 0]返回的是一个一维数组")
pprint(arr3d[1, 0])
# 以上数组子集选择中，返回的数组都是视图
# 4.1.4.1 数组的切片索引
print("\n数组可以通过类似Python列表的语法进行切片")
pprint(arr)
pprint(arr[1:6])
pprint(arr2d)
pprint(arr2d[:2])
pprint(arr2d[:2, 1:])
pprint(arr2d[1][:2])
pprint(arr2d[1, :2])
pprint(arr2d[2, :2])
pprint(arr2d[:, :1])
print("\n对切片表达式赋值时，整个切片都会重新赋值")
arr2d[:2, 1:] = 0
pprint(arr2d)


# 4.1.5 布尔索引
print("\n布尔索引")
# 示例
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
data = np.random.randn(7, 4)
pprint(names)
pprint(data)
print("\n每个名称和data数组中的一行相对应，同时选中所有'Bob'对应的行")
pprint(names == 'Bob')
print("\n索引数组时传入布尔值数组")
pprint(data[names == 'Bob'])
pprint(data[names == 'Bob', 2:])
pprint(data[names == 'Bob', 3])
print("\n选择除'Bob'以外的其他数据：!=")
pprint(names != 'Bob')
pprint(data[~(names == 'Bob')])	# ~对一个通用条件进行取反时使用
cond = names == 'Bob'
pprint(data[~cond])

print("\n数学操作符&(and) |(or)")
mask = (names == 'Bob')|(names == 'Will')
pprint(names)
pprint(mask)
pprint(data[mask])

print("\n将data中所有负数设置为0")
pprint(data)
data[data < 0] = 0
pprint(data)
print("\n利用一维布尔值数组对每一行设置数值")
data[names != 'Joe'] = 7
pprint(data)

# 4.1.6 神奇索引
# 神奇索引：用于描述使用整数数组进行数据索引
arr = np.empty((8, 4))
for i in range(8):
	arr[i] = i
pprint(arr)
print("\n通过传递一个包含指明所需顺序的列表或数组来选取符合特定顺序的子集")
pprint(arr[[4, 3, 0, 6]])
pprint(arr[[-3, -5, -7]])
print("\n传递多个索引数组")
print("reshape具体方法")
arr = np.arange(32).reshape((8, 4))
pprint(arr)
pprint(arr[[1, 5, 7, 2], [0, 3, 1, 2]])
pprint(arr[[1, 5, 7, 2]][:, [0, 3, 1, 2]])
print("神奇索引与切片不同，它总是将数据复制到一个新的数组中")

# 4.1.7 数组转置和换轴
print("\n数组转置和换轴")
print("一种特殊的数据重组形式，可以返回底层数据的视图而不需要复制任何内容")
print("transpose方法，也有特殊的T属性")
arr = np.arange(15).reshape((3,5))
pprint(arr)
pprint(arr.T)

print("\n计算矩阵内积使用np.dot")
arr = np.random.randn(6, 3)
pprint(arr)
pprint(np.dot(arr.T, arr))

print("\n高纬度数组，transpose可以接受包含轴编号的元组，用于置换轴")
arr = np.arange(16).reshape((2, 2, 4))
pprint(arr)
pprint(arr.transpose((1, 0, 2)))


print("\nswapaxes接收一堆轴编号作为参数，并对轴进行调整用于重组数据")
print("swapaxes返回的是数据的视图，而没有对数据进行复制")
pprint(arr)
pprint(arr.swapaxes(1, 2))