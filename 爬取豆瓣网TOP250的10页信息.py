'''
Created on 2018年3月25日
爬虫思路分析：
（1）通过手动浏览获取url
（2）需要爬取的信息：书名、书本的URL链接、作者、出版社和出版时间，书本价格、评分和评价
（3）运用Python中的csv库，把爬取的信息存储在本地的CSV文件中
@author: lenovo
'''
#导入相应的库文件
from lxml import etree
import requests
import csv

#创建csv
fp = open('F:/Learning/Python/pythonLearning/src/Python爬虫/doubanbook.csv', 'wt',
          newline = '', encoding = 'utf-8')
writer = csv.writer(fp)
writer.writerow(('name', 'url', 'author', 'publisher', 'date', 'price', 
                 'rate', 'comment'))        #写入header

#构造urls
urls = []
for i in range(0,250,25):
    urls.append('https://book.douban.com/top250?start={}'.format(str(i)))
    
#加入请求头
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'}

for url in urls:
    html = requests.get(url, headers = headers)
    selector = etree.HTML(html.text)
    infos = selector.xpath('//tr[@class="item"]')
    for info in infos:
        name = info.xpath('td/div/a/@title')[0]
        url = info.xpath('td/div/a/@href')[0]
        book_infos = info.xpath('td/p/text()')[0]
        author = book_infos.split('/')[0]
        publisher = book_infos.split('/')[-3]
        date = book_infos.split('/')[-2]
        price = book_infos.split('/')[-1]
        rate = info.xpath('td/div/span[2]/text()')[0]
        comments = info.xpath('td/p/span/text()')
        comment = comments[0] if len(comments) != 0 else "空"
        writer.writerow(('name', 'url', 'author', 'publisher', 'date', 'price', 
                 'rate', 'comment'))
        
fp.close()