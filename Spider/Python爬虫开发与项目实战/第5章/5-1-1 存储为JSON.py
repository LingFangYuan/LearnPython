import json

import requests
from bs4 import BeautifulSoup


user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}
r = requests.get('http://seputu.com/', headers=headers)
soup = BeautifulSoup(r.text, 'lxml')

content = []
for mulu in soup.find_all(class_='mulu'):
    h2 = mulu.find('h2')
    if h2 is not None:
        l1 = []
        h2_title = h2.string
        # print(h2_title)
        # print('-' * 50)
        for a in mulu.find(class_='box').find_all('a'):
            href = a.get('href')
            box_title = a.get('title')
            l1.append({'href': href, 'box_title': box_title})
            # content = a.string.split()
            # section = content[-2] if len(content) >= 2 else content[-1]
            # sect_name = content[-1]
            # print(href, box_title)
        content.append({'title': h2_title, 'content': l1})
        
with open('qiye.json', 'w', encoding='utf-8') as fp:
    json.dump(content, fp=fp, ensure_ascii=False, indent=4)


