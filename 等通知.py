import requests
import pandas
from bs4 import BeautifulSoup

headers = {
    'cookie': 'sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221830cbf9d91ebd-06dbc3616e14ee-78565470-1327104-1830cbf9d9212e8%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%221830cbf9d91ebd-06dbc3616e14ee-78565470-1327104-1830cbf9d9212e8%22%7D; __bid_n=1830cbf9fae6e5fb5d4207; JSESSIONID=400F5E9A6D71A6E6861C085163AC1767',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
}
url = 'https://www.bkjx.sdu.edu.cn/sanji_list.jsp?urltype=tree.TreeTempUrl&wbtreeid=1010'
r = requests.get(url, headers=headers)
res = r.content
soup = BeautifulSoup(res, 'lxml')
contents = soup.find_all('div', class_='leftNews3')
title_list, date_list, link_list = [], [], []
for content in contents:
    try:
        title = content.find('div', style='float:left').get_text()
    except AttributeError:
        title = ''
    try:
        date = content.find('div', style='float:right;').string
    except AttributeError:
        date = ''
    date_list.append(date)
    title_list.append(title)

li = soup.find('div', class_='newscontent')
for k in li.find_all('a'):
    link = k.get('href')
    link_list.append(link)
link_list = link_list[0:15]
Data = {
    '日期': date_list,
    '标题': title_list,
    '链接': link_list,
}
dataframe = pandas.DataFrame(data=Data)
dataframe.to_excel('山东大学通知.xlsx', index=False, encoding='utf-8')