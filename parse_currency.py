import requests
from bs4 import BeautifulSoup

url = 'https://www.cbr.ru/currency_base/daily/'
soup = BeautifulSoup(requests.get(url).text, 'html.parser')
cur_soup = soup.find('table', class_='data').find_all('td')

cur_name = ['USD', 'EUR', 'CNY']
cur_value = [0, 0, 0]
cur_signs = ['🇺🇸', '🇪🇺', '🇨🇳']
cur_list = []
for i in range(len(cur_name)):
    cur_list.append([cur_value[i], cur_signs[i]])
cur_dict = dict(zip(cur_name, cur_list))


def parse_cur():
    for i, td in enumerate(cur_soup):
        for k in cur_dict.keys():
            if k in td:
                cur_dict[k][0] = round(float(cur_soup[i + 3].text.replace(',', '.')), 2)
    res = ''
    for v in cur_dict.values():
        res += f'{v[1]}{v[0]} '
    return res



