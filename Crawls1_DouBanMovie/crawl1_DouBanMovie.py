#coding:utf-8

# 爬取豆瓣影评上的电影名称

from bs4 import BeautifulSoup
from lxml import html
import xml
import requests

# 要爬取的网页
url = "https://movie.douban.com/chart"
# Get该网页从而获取其HTML内容
response = requests.get(url)
# 用lxml解析器解析该网页内容
soup = BeautifulSoup(response.content, 'lxml')

#print(response.content.decode())
#content = soup.find_all('div', class_ = "pl2")

for k in soup.find_all('div', class_ = 'pl2'):
    a = k.find_all('span')
    print(a[0].string)