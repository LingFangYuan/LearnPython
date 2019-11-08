from urllib.request import urlretrieve
from urllib.request import urljoin
import os
from lxml import etree
import requests


def schedule(blocknum, blocksize, totalsize):
    '''
    blocknum: 已下载的数据块
    blocksize: 数据块的大小
    totalsize: 远程文件的大小
    '''
    per = 100.0 * blocknum * blocksize / totalsize
    if per > 100:
        per = 100
    print('当前下载进度： %d' % per)


def join_url(url):
    if not url.startswith('http'):
        url = urljoin(base_url, url)
    return url


def download_file(img_urls, file_type, suffix):
    if not os.path.exists(file_type):
        os.mkdir(file_type)
    i = 0
    for img_url in img_urls:
        img_url = join_url(img_url)
        print(img_url)
        file_path = os.path.join(file_type, file_type + str(i) + '.' + suffix)
        urlretrieve(img_url, file_path, schedule)
        i += 1


def open_url(url):
    url = join_url(url)
    print(url)
    user_agent = 'Mozillia/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Ageng': user_agent}
    r = requests.get(url, headers=headers)
    html = etree.HTML(r.text)
    return html

base_url = 'https://www.ivsky.com/tupian/ziranfengguang/'
html = open_url(base_url)
img_urls = html.xpath('.//img/@src')
download_file(img_urls, 'img', 'jpg')
