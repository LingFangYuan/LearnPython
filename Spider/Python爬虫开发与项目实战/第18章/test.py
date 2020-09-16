from pyquery import PyQuery as pq
from lxml import etree
# d = pq('<html></html>')
# d = pq(etree.fromstring('<html></html>'))
# d = pq('http://www.baidu.com')
# d = pq(filename='index.html')

# p = pq('<p id="hello" class="hello"></p>')#('p')
# print(p.attr('id'))
# print(p.attr['id'], p.attr.id)
# print(p.attr('id', 'plop'))
# print(p.attr('id', 'hello'))
# print(p.attr(id='hello1', class_='hello1'))
# p.attr.class_ = 'world'
# p.add_class('!!!')
# print(p)
# print(p.css('font-size', '15px'))
# print(p.attr.style)

# d = pq('<p class="hello" id="hello">you know Python rocks</p>')
# d('p').append(' check out <a href="http://123.com"><span>1234</span></a>')
# print(d)
# p = d('p')
# p.prepend('check out <a href="http://123.com"><span>1234</span></a> ')
# print(p)

# html_cont = '''
# <div>
#     <ul>
#         <li class="one">first item</li>
#         <li class="two"><a href="link2.html">second</a></li>
#         <li class="four"><a href="link3.html">third</a></li>
#         <li class="three"><a href="link4.html"><span class="bold">fourth</span>
#             </a></li>
#     </ul>
# </div>

# '''
# doc = pq(html_cont)
# lis = doc('li')
# for li in lis.items():
#     print(li.html())

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.90 Safari/537.36 2345Explorer/9.3.2.17331'}

# r = requests.get('https://movie.douban.com/subject/26794435/',
#                  'lxml', headers=headers)
# r.encoding = 'utf-8'
# with open('test.html', 'w', encoding='utf-8') as f:
#     f.write(r.text)
with open('test.html', 'r', encoding='utf-8') as f:
    doc = pq(f.read())
info = doc('#info').text()
print(dict(tuple(l.split(':')) for l in info.split('\n') if len(l.split(':')) == 2))
