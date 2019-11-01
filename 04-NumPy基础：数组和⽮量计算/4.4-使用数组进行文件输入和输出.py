# -*- coding: utf-8 -*-
"""
@author: 东风
@file: 4.4-使用数组进行文件输入和输出.py
@time: 2019/10/12 17:38
"""

import numpy as np
from pprint import pprint

print("np.save和np.load是高效存储硬盘数据的两大工具函数")
# 保存
arr = np.arange(10)
# pprint(arr)
np.save('some_array', arr)

# 载入
# pprint(np.load('some_array.npy'))

print("\n使用np.savez将数组作为参数传递给该函数，用于在未压缩文件中保存多个数组")
np.savez('array_archive.npz', a=arr, b=arr)

arch = np.load('array_archive.npz')
pprint(arch['b'])

print("\n如数据已经压缩好了，使用np.savez_compressed将数据存入已经压缩的文件")
np.savez_compressed('arrays_compreseed.npz', a=arr, b=arr)



