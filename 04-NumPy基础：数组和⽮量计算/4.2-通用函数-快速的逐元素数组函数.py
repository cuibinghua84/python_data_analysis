# -*- coding: utf-8 -*-
"""
@author: 东风
@file: 4.2-通用函数-快速的逐元素数组函数.py
@time: 2019/10/12 17:19
"""
import numpy as np
from pprint import pprint

# print("\n高纬度数组，transpose可以接受包含轴编号的元组，用于置换轴")
# arr = np.arange(16).reshape((2, 2, 4))
# pprint(arr)
# pprint(arr.transpose((1, 0, 2)))

# print("\nswapaxes接收一堆轴编号作为参数，并对轴进行调整用于重组数据")
# print("swapaxes返回的是数据的视图，而没有对数据进行复制")
# pprint(arr)
# pprint(arr.swapaxes(1, 2))

print("unfunc的逐元素转换函数：一元通用函数")
arr = np.arange(10)
pprint(arr) # array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

pprint(np.sqrt(arr))
"""
array([0.        , 1.        , 1.41421356, 1.73205081, 2.        ,
       2.23606798, 2.44948974, 2.64575131, 2.82842712, 3.        ])
"""

pprint(np.exp(arr))
"""
array([1.00000000e+00, 2.71828183e+00, 7.38905610e+00, 2.00855369e+01,
       5.45981500e+01, 1.48413159e+02, 4.03428793e+02, 1.09663316e+03,
       2.98095799e+03, 8.10308393e+03])
"""
print("\nunfunc的逐元素转换函数：二元通用函数")
x = np.random.randn(8)
y = np.random.randn(8)
pprint(x)
"""
array([-1.60328565, -0.66841324,  0.63647093, -0.55357148,  0.64602241,
        0.64833307,  1.1699383 ,  0.3028686 ])
"""
pprint(y)
"""
array([-0.68622641,  0.18200928,  0.99561407,  0.51067792,  0.18646972,
       -0.0215062 ,  0.78243755,  1.62363713])
"""
pprint(np.maximum(x, y)) # maximum：逐元素地将x和y中元素的最大值计算出来
"""
array([-0.68622641,  0.18200928,  0.99561407,  0.51067792,  0.64602241,
        0.64833307,  1.1699383 ,  1.62363713])
[Finished in 0.8s]
"""

print("\nunfunc的逐元素转换函数：返回多个数组的")
arr = np.random.randn(7) * 5
pprint(arr)
remainder, whole_part = np.modf(arr)
pprint(remainder)
"""
array([-1.49100302, 11.40916737, -2.7395339 ,  6.58535995,  2.58344602,
       -9.48474331,  0.1951148 ])
"""
pprint(whole_part)
"""
array([-0.49100302,  0.40916737, -0.7395339 ,  0.58535995,  0.58344602,
       -0.48474331,  0.1951148 ])
"""
print("\n通用函数接收可选参数out，可对数组按位操作")
pprint(arr)
"""
array([ 1.89347255, -0.20846612,  0.80343677, -6.89803684, -4.94189114,
        1.38511569,  4.66166916])
"""
pprint(np.sqrt(arr))
"""
array([1.37603508,        nan, 0.89634635,        nan,        nan,
       1.17690938, 2.15908989])
"""
pprint(np.sqrt(arr, arr))
"""
array([1.37603508,        nan, 0.89634635,        nan,        nan,
       1.17690938, 2.15908989])
"""
pprint(arr)
"""
array([1.37603508,        nan, 0.89634635,        nan,        nan,
       1.17690938, 2.15908989])
"""

"""
一元通函数
abs、fabs：逐元素地计算整数、浮点数或复数的绝对值
sqrt：计算每个元素的平方根
square：计算每个元素的平方

二元通函数
add：将数组的对应元素相加
subtract：在第二个数组中，将第一个数组中包含的元素去除
multiply：将数组的对应元素相乘
divide，floor_divide：除或整除
power：将第二个数组的元素作为第一个元素对应元素的幂次方
maximum，fmax：逐个元素计算最大值
minimum，fmin：逐个元素计算最小值
mod：按元素求模计算
copysign：将第一个数组的符号值改为第二个数组的符号值
greater，greater_equal,less：进行逐个元素的比较，返回布尔值数组（数学
less_equal,equal,not_equal操作符> >= < <= == !=效果一致）
logical_and,logical_or:进行逐个元素的逻辑操作
logical_xor:
"""