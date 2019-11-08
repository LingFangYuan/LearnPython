import requests
import chardet


# # 1 一个完整的请求与响应模型
# r = requests.get('http://www.baidu.com')
# print(vars(r))
# print(r.content.decode('utf-8'))

# postdata = {'key': 'value'}
# r = requests.post('http://www.xxxxx.com/login', data=postdata)
# print(r.content)

# params = {'Keywords': 'qiyeboy', 'pageindex': 2}
# r = requests.get('http://zzk.cnblogs.com/s/blogpost', params=params)
# print(r.status_code, r.url)


# # 2 响应与编码
# r = requests.get('http://www.baidu.com', stream=True)
# # print('content-->', r.content)
# # print('text-->', r.text)
# # print('encoding-->', r.encoding)
# # r.encoding = 'utf-8'
# # print('new text-->', r.text)
# print(chardet.detect(r.content))
# r.encoding = chardet.detect(r.content)['encoding']
# print(r.text)
# print(r.raw.read(10))


# # 3 请求头headers处理 和 Cookie处理
# user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
# headers = {'User-Agent': user_agent}
# cookies = {'name': 'qiye', 'age': '10'}
# r = requests.get('http://www.baidu.com', headers=headers, cookies=cookies)
# print(r.text)
# for cookie in r.cookies.keys():
#     print(cookie, ':', r.cookies.get(cookie))


# # 4 响应码code和响应头headers处理
# r = requests.get('http://www.baidu.com')
# if r.status_code == requests.codes.ok:
#     print(r.status_code)
#     print(r.headers)
#     print(r.headers.get('Content-Type'))
#     print(r.headers['Content-Type'])
# else:
#     r.raise_for_status()


# # 5 Cookie自动处理 
# login_url = 'http://www.xxxxxxx.com/login'
# s = requests.Session()
# r = s.get(login_url, allow_redirects=True)
# data = {'name': 'qiye', 'passwd': 'qiye'}
# r = s.post(login_url, data=data, allow_redirects=True)
# print(r.text)


# 6 重定向与历史信息
r = requests.get('http://172.30.1.53:18480/pasoreport-web/')
print(r.url)
print(r.status_code)
print(r.history)
