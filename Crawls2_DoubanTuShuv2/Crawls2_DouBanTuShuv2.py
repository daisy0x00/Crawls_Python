#coding:utf-8

from lxml import etree
import requests
import time
import csv

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrower/6.1.2.2107.204 Safari/537.36'
}

csv_file = open('DouBanTop250.csv', 'w', encoding = 'utf-8')
csv_writer = csv.writer(csv_file, delimiter = ',')

for a in range(10):
    url = 'https://book.douban.com/top250?start={}'.format(a*25)
    data = requests.get(url, headers = header).text

    s = etree.HTML(data)
    file = s.xpath('//*[@id="content"]/div/div[1]/div/table')
    time.sleep(3)

    for div in file:
        title = div.xpath("./tr/td[2]/div[1]/a/@title")[0]
        href = div.xpath("./tr/td[2]/div[1]/a/@href")[0]
        author = div.xpath("./tr/td[2]/p/text()")[0]
        score = div.xpath("./tr/td[2]/div[2]/span[2]/text()")[0]
        nums = div.xpath("./tr/td[2]/div[2]/span[3]/text()")[0].strip('(').strip().strip(')').strip()
        scrible = div.xpath("./tr/td[2]/p[2]/span/text()")

        if len(scrible) > 0:
            print("{}, {}, {}, {}, {}, {}".format(title, href, author, score, nums, scrible[0]))
            csv_writer.writerow([title, href, author, score, nums, scrible[0]])
        else:
            print("{}, {}, {}, {}, {}".format(title, href, author, score, nums))
            csv_writer.writerow([title, href, author, score, nums])






###
    #title #href  #score #num #scrible
    #//*[@id="content"]/div/div[1]/div/table[1]/tr/td[2]/div[1]/a/@title
    #//*[@id="content"]/div/div[1]/div/table[1]/tr/td[2]/div[1]/a/@href
    #//*[@id="content"]/div/div[1]/div/table[1]/tr/td[2]/div[2]/span[2]
    #//*[@id="content"]/div/div[1]/div/table[1]/tr/td[2]/div[2]/span[3]
    #//*[@id="content"]/div/div[1]/div/table[1]/tr/td[2]/p[2]/span

    #other
    #//*[@id="content"]/div/div[1]/div/table/tr/td[2]/p[1]

###
    #title
    #//*[@id="content"]/div/div[1]/div/table[1]/tbody/tr/td[2]/div[1]/a
    #//*[@id="content"]/div/div[1]/div/table[1]/tr/td[2]/div[1]/a/@title

    #href
    #//*[@id="content"]/div/div[1]/div/table[1]/tbody/tr/td[2]/div[1]/a
    #//*[@id="content"]/div/div[1]/div/table[1]/tr/td[2]/div[1]/a

    #author
    #//*[@id="content"]/div/div[1]/div/table[1]/tbody/tr/td[2]/p[1]
    #//*[@id="content"]/div/div[1]/div/table[1]/tr/td[2]/p[1]

    #score
    #//*[@id="content"]/div/div[1]/div/table[1]/tbody/tr/td[2]/div[2]/span[2]
    #//*[@id="content"]/div/div[1]/div/table[1]/tr/td[2]/div[2]/span[2]

    #num
    #//*[@id="content"]/div/div[1]/div/table[1]/tbody/tr/td[2]/div[2]/span[3]
    #//*[@id="content"]/div/div[1]/div/table[1]/tr/td[2]/div[2]/span[3]

    #scrible
    #//*[@id="content"]/div/div[1]/div/table[1]/tbody/tr/td[2]/p[2]/span
    #//*[@id="content"]/div/div[1]/div/table[1]/tr/td[2]/p[2]/span

