# -*- coding: utf-8 -*-
"""
@author: 东风
@file: movie_lens.py
@time: 2019/10/10 9:55
"""
"""
数据资源背景
数据集包含6000个用户，对4000部电影的100万个评分；
分为三个表格：评分、用户信息和电影信息
"""

import pandas as pd
from pprint import pprint

# 用pandas.read_table将每个表加载到一个pandas DataFrame对象中

# 让展示内容少一点
pd.options.display.max_rows = 10
# 用户信息（users.dat表，数据无表目信息）
unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
users = pd.read_csv('D:/data/pydata_book2/datasets/movielens/users.dat', sep='::', header=None, names=unames, engine='python')

# 评分信息
rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_csv('D:/data/pydata_book2/datasets/movielens/ratings.dat', sep='::', header=None, names=rnames, engine='python')

# 电影信息
mnames = ['movie_id', 'title', 'genres']
movies = pd.read_csv('D:/data/pydata_book2/datasets/movielens/movies.dat', sep='::', header=None, names=mnames, engine='python')

# 通过切片来查看每个DataFrame的前几行来验证一切是否成功
# print(users[:5])
# pprint(users[:5])
# print(ratings[:5])
# print(movies[:5])
# print(ratings)

# 按照性别和年龄计算某个电影的平均评分
"""
1、使用pandas的合并功能
2、将ratings表与users表合并
3、然后将结果与movies表数据合并
4、pandas根据重叠名称推断哪些列用作合并（或连接）的键位
"""

data = pd.merge(pd.merge(ratings, users), movies)
# print(data[:5])

# 按性别分级的每部电影的平均电影评分
# mean_ratings = data.pivot_table('rating', index='title', columns='gender', aggfunc='mean')
# print(mean_ratings[:5])

# 按标题进行分组，并使用size()为每个标题获取一个元素是各分组大小的Series
ratings_by_title = data.groupby('title').size()
# print(ratings_by_title[:10])

# 过滤小于250个评分的电影
active_titles = ratings_by_title.index[ratings_by_title >= 250]
# print(active_titles)

# 从mean_ratings中选取所需要的行
# mean_ratings = mean_ratings.loc[active_titles]
# print(mean_ratings)

# 看女性观众的top电影，按F类降序排序
# top_female_ratings = mean_ratings.sort_values(by='F', ascending=False)
# print(top_female_ratings[:10])

# 测量评价分歧
# 查找男性和女性观众之间最具分歧的电影，通过计算均值差
# mean_ratings['diff'] = mean_ratings['M'] - mean_ratings['F']
# 按照‘diff’排序产生评分差异最大的电影
# sorted_by_diff = mean_ratings.sort_values(by='diff')
# print(sorted_by_diff[:10])

# 转换行的顺序，并切出top10的房，获得男性更喜欢但女性评分不高的电影
# print(sorted_by_diff[::-1][:10])

# 不是通过性别而引起的最大差异的电影，通过评分的方差或标准差来衡量的
rating_std_by_title = data.groupby('title')['rating'].std()
rating_std_by_title = rating_std_by_title.loc[active_titles]
print(rating_std_by_title.sort_values(ascending=False)[:10])