#-*-coding:utf-8-*-

#s1-start
import requests
from bs4 import BeautifulSoup

class stock:
 name = 'a'
 tag = '1'
 startprice = 0
 currprice = 0

stocks = list()
for i in range(9):
 stocks.append(stock())

stocks[0].name = 'cj대한통운'
stocks[0].tag = '000120'
stocks[1].name = 'nh투자증권우'
stocks[1].tag = '005945'
stocks[2].name = 'lg유플러스'
stocks[2].tag = '032640'
stocks[3].name = '다나와'
stocks[3].tag = '119860'
stocks[4].name = '미래에셋대우우'
stocks[4].tag = '006805'
stocks[5].name = '한화3우b'
stocks[5].tag = '00088K'
stocks[6].name = 'cj우'
stocks[6].tag = '001045'
stocks[7].name = 'cj cgv'
stocks[7].tag = '079160'
stocks[8].name = '한화'
stocks[8].tag = '000880'


#==================================================
#s2-workstart
url = "https://finance.naver.com/item/main.nhn?code="

for s in stocks:
 rvurl = url + s.tag
 html = requests.get(rvurl)
 soup = BeautifulSoup(html.content,'html.parser')
  
 
 today = soup.find('div',class_='today')
 no_today = today.find('p',class_='no_today')
 price = no_today.find_all('em',class_='no_down')
 price = no_today.find_all('span',class_='blind') 

 print(price)
 print('==============') 
 
