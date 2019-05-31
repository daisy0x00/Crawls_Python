#coding:utf-8
# 该代码的功能，爬取豆瓣评书Top250，并将爬取的数据保存在DouBanTop250.csv文件中

from lxml import etree
import requests
import time
import csv

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}

csv_file = open('DouBanTop250.csv', 'w')
csv_writer = csv.writer(csv_file, delimiter = ',')

for a in range(10):
    url = 'https://book.douban.com/top250?start={}'.format(a*25)
    data = requests.get(url, headers = header).text

    s = etree.HTML(data)
    file = s.xpath('//*[@id="content"]/div/div[1]/div/table')
    print(file)
    time.sleep(3)

    for div in file:
        title = div.xpath("./tr/td[2]/div[1]/a/@title")[0]
        href = div.xpath("./tr/td[2]/div[1]/a/@href")[0]
        score = div.xpath("./tr/td[2]/div[2]/span[2]/text()")[0]
        num = div.xpath("./tr/td[2]/div[2]/span[3]/text()")[0].strip("(").strip().strip(")").strip()
        scrible = div.xpath("./tr/td[2]/p[2]/span/text()")

        if len(scrible) > 0:
            csv_writer.writerow([title, href, score, num, scrible[0]])
            print("{}, {}, {}, {}, {}\n".format(title, href, score, num, scrible[0]))
        else:
            csv_writer.writerow([title, href, score, num])
            print("{}, {}, {}, {}\n".format(title, href, score, num))