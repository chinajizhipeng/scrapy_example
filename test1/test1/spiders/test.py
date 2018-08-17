# -*- coding: UTF-8 -*-
import requests
response = requests.get("http://news.qut.edu.cn/lgyw.htm")
print(response.text)
print(response.status_code) #状态码
from pyquery import PyQuery as pq
doc = pq(url='http://news.qut.edu.cn/lgyw.htm')
print(doc)
