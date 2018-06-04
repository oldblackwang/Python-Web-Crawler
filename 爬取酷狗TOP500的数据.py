'''
Created on 2018年2月8日
爬虫思路分析：
    1.爬取内容为酷狗榜单中酷狗TOP500的音乐信息
    2.网页版酷狗不能手动翻页进行下一步浏览，但通过观察第一页的URL：
      http://www.kugou.com/yy/rank/home/1-8888.html?from=rank
              发现将数字1换成2即为第二页
              每页显示22首歌曲，所以总共需要23个URL
    3.需要爬取的信息：排名情况，歌手，歌曲名，歌曲时间
@author: lenovo
'''
#导入需要的库
import requests                     #用于请求网页获取网页数据
from bs4 import BeautifulSoup       #用于解析网页数据
import time                         #其中的sleep()方法可以让程序暂停

#加入请求头,用于伪装为浏览器，便于爬虫的稳定性
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'
    }

def get_info(url):
    '''定义获取信息的函数'''
    wb_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(wb_data.text,'html.parser')
    ranks = soup.select('#rankWrap > div.pc_temp_songlist > ul > li > span.pc_temp_num')
    titles = soup.select('#rankWrap > div.pc_temp_songlist > ul > li > a')
    times = soup.select('#rankWrap > div.pc_temp_songlist > ul > li > span.pc_temp_tips_r > span')
    for rank, title, time in zip(ranks, titles, times):
        data = {
            'rank':rank.get_text().strip(),
            'singer':title.get_text().split('-')[0],
            'song':title.get_text().split('-')[1],
            'time':time.get_text().strip()
            }
        print(data)         #爬取信息并按字典格式打印

#程序主入口
if __name__ == '__main__':  
    '''__name__ 是当前模块名，当模块被直接运行时模块名为 __main__ 
                这句话的意思就是，当模块被直接运行时，以下代码块将被运行，当模块是被导入时，代码块不被运行
    '''
    urls = []
    for i in range(1,24):
        urls.append('http://www.kugou.com/yy/rank/home/{}-8888.html?from=rank'.format(str(i)))   #构造多页URL
    for url in urls:
        get_info(url)
        time.sleep(1)       #睡眠1秒
    
    
    
    
    
    
    