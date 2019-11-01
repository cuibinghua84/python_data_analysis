# -*- coding: utf-8 -*-
"""
NumPy：（Numerical Python）是目前Python数值计算中最为重要的基础包
    ndarray，一种高效多维数组，提供了基于数组的便捷算术操作以及灵活的广播功能
    对所有数据进行快速的矩阵计算，并对内存映射文件进行操作
    线性代数、随机数生成以及傅里叶变换功能
    用于连接NumPy与C、C++和FORTRAN语言类库C语言API

作者关注的内容
    1、数据处理、清洗、构造子集、过滤、变换以及其他计算中进行快速的向量化计算
    2、常见的数组算法、比如sort、unique以及set操作等
    3、高效的描述性统计和聚合/概述数据
    4、数据排列和相关数据操作，例如对异构数据进行merge和join
    5、使用数组表达式来表明条件逻辑，代替if-elif-else条件分支的循环
    6、分组数据操作(聚合、变换以及函数式操作)
NumPy的重要性
    1、它的设计对于包含有大量数组的数据非常有效
    2、NumPy在内部将数据存储在连续的内存块上
    3、可以针对全量数据进行复杂计算而不需要些Python循环

1、NumPy ndarray: 多维数组对象
2、通用函数：快速的逐元素数组函数
3、使用数组进行面向数组编程
4、使用数组进行文件输入和输出
5、线性代数
6、伪随机数生成
7、示例：随机漫步
8、本章小结
9、
"""

# NumPy数据包含100万个整数和同样数据内容的Python列表进行比较
import numpy as np
from pprint import pprint

my_arr = np.array(1000000)
my_list = list(range(1000000))

"""
%time for _ in range(10): my_arr2 = my_arr * 2
Wall time: 0 ns
%time for _ in range(10): my_list2 = [x * 2 for x in my_list]
Wall time: 1.85 s
"""







