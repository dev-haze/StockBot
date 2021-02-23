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
murl = 'https://m.stock.naver.com/item/main.nhn#/stocks/'

for s in stocks:
 rvurl = murl + s.tag + '/total'
 html = requests.get(rvurl)
 soup = BeautifulSoup(html.content,'html.parser')

 #price = soup.find(attrs={'class':'stock_price stock_dn'})
 #price = soup.find('strong',{'class':'stock_price'})
 #price = soup.find_all(attrs={'class':'price_wrp'})
 #price = soup.find_all('div',class_='price_wrp')
 #price = soup.find_all(attrs={"class":"stock_price", "class":"stock_dn"})
 #price = soup.find_all(attrs={"class":"stock_price"})
 price = soup.find_all(attrs={"class":"flick-ct"})

 
  
 print(price)
 print("----------")




