# -*- coding: utf-8 -*-
"""
@author: 东风
@file: 6.3-与数据库交互.py
@time: 2019/10/22 11:24
"""

import sqlite3
from pprint import pprint
import pandas as pd
import sqlalchemy as sqla

# 生成一个SQLite数据库
# query = """
#     create table test
#     (a varchar(20), b varchar(20),
#     c real, d integer
#     );"""
con = sqlite3.connect('mydata.sqlite')
# con.execute(query)
# con.commit()

# 插入数据
# data = [('Atlanta', 'Georgia', 1.25, 6), ('Tallahassee', 'Florida', 2.6, 3), ('Sacramento', 'California', 1.7, 5)]
# stmt = "insert into test values(?, ?, ?, ?)"
# con.executemany(stmt, data)
# con.commit()

# 查询数据
cursor = con.execute('select * from test')
rows = cursor.fetchall()
pprint(rows)

# 将元组的列表传递给DataFrame构造函数，还需要包含在游标的description属性中
# pprint(cursor.description)
pprint(pd.DataFrame(rows, columns=[x[0] for x in cursor.description]))
print()
# SQLAlchemy项目是一个流行的Python SQL工具包，抽象去除了SQL数据库之间的许多常见异常。
# pandas有一个read_sql函数允许你从通用的SQLAlchemy连接中轻松地读取数据
db = sqla.create_engine('sqlite:///mydata.sqlite')
pprint(pd.read_sql('select * from test', db))