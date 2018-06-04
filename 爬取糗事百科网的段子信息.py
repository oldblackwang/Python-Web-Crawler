'''
Created on 2018年2月10日
利用request库和正则表达式方法，爬取糗事百科网中“文字”专题的段子信息，并把爬取的数据存储到本地文件中
爬虫思路分析：
1.爬取内容为爬取糗事百科网中“文字”专题的段子信息
2.构建URL
    第一页：https://www.qiushibaike.com/text/page/1/
    第二页：https://www.qiushibaike.com/text/page/2/
    第三页：https://www.qiushibaike.com/text/page/3/
    第四页：https://www.qiushibaike.com/text/page/4/
3.需要爬取的信息：用户ID，用户等级，用户性别，发表段子文字信息，好笑数量和评论数量
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

#初始化列表，用于装入爬虫信息
info_lists = []

#定义获取用户性别的函数
def judgment_sex(class_name):
    '''获取用户性别'''
    if class_name == 'manIcon':
        return '男'
    else:
        return '女'
    
#定义获取信息的函数
def get_info(url):
    res = requests.get(url, headers=headers)
    ids = re.findall('<h2>(.*?)</h2>', res.text, re.S)
    levels = re.findall('<div class="articleGender \D+Icon">(.*?)</div>', res.text, re.S)
    sexs = re.findall('<div class="articleGender (.*?)">', res.text, re.S)
    contents = re.findall('<div class="content">.*?<span>(.*?)</span>', res.text, re.S)
    laughs = re.findall('<span class="stats-vote"><i class="number">(\d+)</i>', res.text, re.S)
    comments = re.findall('<i class="number">(\d+)</i>', res.text, re.S)
    for id, level, sex, content, laugh, comment in zip(ids, levels, sexs, contents, laughs, comments):
        info = {
            '用户ID':id,
            '用户等级':level,
            '用户性别':judgment_sex(sex),
            '段子内容':content,
            '好笑值':laugh,
            '评论数':comment
            }
        info_lists.append(info)     #获取数据，并追加到列表中
    
#程序主入口
if __name__ == '__main__':
        urls = []
        for i in range(1,14):
            urls.append('https://www.qiushibaike.com/text/page/{}/'.format(str(i)))
        for url in urls:
            get_info(url)
            time.sleep(1)
            for info_list in info_lists:
                f = open('F:/学习使我快乐/Python/pythonLearning/src/Python爬虫/糗事百科网段子.txt', 'a+')
                
                try:
                    f.write('用户ID：' + info_list['用户ID'] + '\n')
                    f.write('用户等级：' + info_list['用户等级'] + '\n')
                    f.write('用户性别：' + info_list['用户性别'] + '\n')
                    f.write('段子内容：' + info_list['段子内容'] + '\n')
                    f.write('好笑值：' + info_list['好笑值'] + '\t\t')
                    f.write('评论数：' + info_list['评论数'] + '\n\n')
                    f.close()
                except UnicodeEncodeError:
                    pass
            
    
    
    