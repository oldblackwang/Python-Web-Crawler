'''
Created on 2018年2月8日

@author: lenovo
'''
import requests
from bs4 import BeautifulSoup

headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'
    }

def get_info(url):
    wb_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(wb_data.text, 'html.parser')
    for i in range(3,35):
        ranks = soup.select('#rank_js > div.left_box > div.rank_data > table > tbody > tr:nth-of-type('+ str(i) +') > td:nth-of-type(1)')
        teams = soup.select('#rank_js > div.left_box > div.rank_data > table > tbody > tr:nth-of-type('+ str(i) +')  > td.left > a')
        wins = soup.select('#rank_js > div.left_box > div.rank_data > table > tbody > tr:nth-of-type('+ str(i) +')  > td:nth-of-type(3)')
        loses = soup.select('#rank_js > div.left_box > div.rank_data > table > tbody > tr:nth-of-type('+ str(i) +')  > td:nth-of-type(4)')
        rates = soup.select('#rank_js > div.left_box > div.rank_data > table > tbody > tr:nth-of-type('+ str(i) +')  > td:nth-of-type(5)')
        for rank, team, win, lose, rate in zip(ranks, teams, wins, loses, rates):
            data = {
                '排名':rank.get_text().strip(), 
                '球队':team.get_text().strip(), 
                '胜场数':win.get_text().strip(), 
                '负场数':lose.get_text().strip(), 
                '胜率':rate.get_text().strip()
                }
            print(data)
        
if __name__ == '__main__':
    url = 'https://nba.hupu.com/standings'
    get_info(url)

