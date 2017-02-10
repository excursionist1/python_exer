import requests
from bs4 import BeautifulSoup

res = requests.get('http://www.yes24.com/24/category/More/001001003?ElemNo=3&ElmSeq=1')

soup = BeautifulSoup(res.text, 'lxml')

elem_goods = soup.find(attrs={'id': 'category_layout'}).find_all('tr')[0]\
            .find('td', attrs={'class': 'goodsTxtInfo'})

title = elem_goods.find_all('p')[0].find('a').text
author = elem_goods.find('div', attrs = {'class': 'aupu'}).find('a').text

print(author)


