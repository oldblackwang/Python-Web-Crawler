'''
Created on 2018年2月9日
利用request库和正则表达式方法，爬取《斗破苍穹》全文小说，并把爬取的数据存储到本地文件中
爬虫思路分析：
1.爬取内容：《斗破苍穹》全文小说
2.获取URL：
第一章：http://www.doupoxs.com/doupocangqiong/2.html
第二章：http://www.doupoxs.com/doupocangqiong/5.html
第三章：http://www.doupoxs.com/doupocangqiong/6.html
第四章：http://www.doupoxs.com/doupocangqiong/7.html
第五章：http://www.doupoxs.com/doupocangqiong/8.html
发现从第二章往后规律很明显，故从第一章开始构造URL，中间有404错误就跳过不爬取
3.需要爬取的信息为全文的文字信息
4.运用Python对文件的操作，把爬取的信息存储在本地的TXT文件中
@author: lenovo
'''
#导入相应的库文件
import requests
import re
import time

#加入请求头
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'
    }

#新建TXT文档，模式为追加
f = open('F:/学习使我快乐/Python/pythonLearning/src/Python爬虫/斗破苍穹全本.txt','a+')

#定义获取信息的函数
def get_info(url):
    res = requests.get(url, headers=headers)
    if res.status_code == 200:      #判断请求码是否为200
        contents = re.findall('<p>(.*?)</p>', res.content.decode('utf-8'), re.S)
        for content in contents:
            f.write(content+'\n')
    else:
        pass                        #不为200就跳过
    
#程序主入口
if __name__ == '__main__':
    urls = []
    for i in range(2, 1666):
        urls.append('http://www.doupoxs.com/doupocangqiong/{}.html'.format(str(i)))
    for url in urls:
        get_info(url)
        time.sleep(1)

f.close()








