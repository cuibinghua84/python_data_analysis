# -*- coding: utf-8 -*-
"""
@author: 东风
@file: 6.3-与WebAPI交互.py
@time: 2019/10/22 11:23
"""

from pprint import pprint
import requests
import pandas as pd

url = 'https://api.github.com/repos/pandas-dev/pandas/issues'
resp = requests.get(url)
# print(resp)

data = resp.json()
# pprint(data[0]['title'])

issues = pd.DataFrame(data, columns=['number', 'title', 'labels', 'state'])
pprint(issues[:20])
