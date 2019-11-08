from urllib.request import urlopen, Request
from urllib.request import build_opener, HTTPCookieProcessor
from urllib.request import HTTPError, ProxyHandler, install_opener
from urllib.error import URLError
from urllib.parse import urlencode
from http import cookiejar

# # 1 GET 请求
# responce = urlopen('http://www.zhihu.com')
# html = responce.read().decode('utf-8')
# print(html)

# requet = Request('http://www.zhihu.com')
# responce = urlopen(requet)
# html = responce.read().decode('utf-8')
# print(html)

# # 2 POST请求 header处理
# url = 'http://www.xxxxx.com/login'
# user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
# referer = 'http://www.xxxxx.com/'
# postdata = {'username': 'qiye',
#             'password': 'qiye_pass'}
# headers = {'User-Agent': user_agent, 'Referer': referer}
# data = urlencode(postdata)
# request = Request(url, data, headers) # request = Request(url); request.add_header('User-Agent', user_agent); request.add_header('Referer', referer); request.add_data(data)
# responce = urlopen(request)
# html = responce.read().decode('utf-8')
# print(html)

# # 3 Cookie处理
# # 自动处理
# cookie = cookiejar.CookieJar()
# opener = build_opener(HTTPCookieProcessor(cookie))
# responce = opener.open('http://www.zhihu.com')
# for item in cookie:
#     print(item.name + ': ' + item.value)

# # 手动处理
# opener = build_opener()
# opener.addheaders.append(('Cookie', 'email=' + 'xxxxxxxx@163.com'))
# request = Request('http://www.zhihu.com/')
# responce = opener.open(request)
# print(responce.headers)
# retdata = responce.read().decode('utf-8')

# # 4 Timeout设置超时
# request = Request('http://www.zhihu.com')
# responce = urlopen(request, timeout=2)
# html = responce.read().decode('utf-8')
# print(html)

# # 5 获取HTTP响应码
# try:
#     responce = urlopen('http://www.zhihu.com')
#     print(responce.getcode())
# except HTTPError as e:
#     if hasattr(e, 'code'):
#         print('Error code:', e.code)
# except URLError as e:
#     for attr in dir(e):
#         if not attr.startswith('__') and attr != 'characters_written':
#             print('Error ' + attr + ': ', repr(getattr(e, attr)))

# # 6 重定向
# responce = urlopen('http://www.zhihu.com')
# print(responce.geturl())

# # 7 Proxy的设置
# proxy = ProxyHandler({})
# opener = build_opener(proxy)
# responce = opener.open('http://www.zhihu.com/')
# print(responce.read().decode('utf-8'))
