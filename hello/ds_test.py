import requests
from bs4 import BeautifulSoup
import re
import itertools

res = requests.get("http://www.yes24.com/24/category/More/001001003?ElemNo=3&ElemSeq=1&PageNumber=1")

soup = BeautifulSoup(res.text, 'lxml')
date_re = re.compile(r'(\d{4}).\s+(\d{2}).')

elem_tr_list = soup.find(attrs={'id': 'category_layout'}).find_all('tr')

for tr in elem_tr_list:
    elem_td = tr.find('td', attrs={'class': 'goodsTxtInfo'})

    if elem_td:
        title = elem_td.find_all('p')[0].find('a').text
        author = elem_td.find('div', attrs={'class': 'aupu'}).find('a').text
        publisher = elem_td.find('div', attrs={'class': 'aupu'}).find_all('a')[1].text
        pub_date_text = elem_td.find('div', attrs={'class': 'aupu'}).text

        pub_date = date_re.findall(pub_date_text)
        price = elem_td.find_all('p')[1].find('span', attrs={'class': 'priceB'}).text

        md_book = [str(title).strip(), author, publisher, pub_date[0], price]
        print(title, author, publisher, pub_date, price)




