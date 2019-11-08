import re

import bs4
from bs4 import BeautifulSoup



html_str = """
     <html><head><title>The Dormouse's story</title></head>
     <body>
     <p class="title"><b id="b1">The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
     <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
     <a href="http://example.com/lacie" class="sister" id="link2"><!-- Lacie --></a> and
     <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
     and they lived at the bottom of a well.</p>
     <p class="story">...</p>
     </body></html>
     """

soup = BeautifulSoup(html_str, 'lxml')

# CSS选择器
print('通过标记名称查找：')
print('直接查找title标记：')
print(soup.select('title'))
print('逐层查找title标记：')
print(soup.select('html head title'))
print('查找head下面的title标记：')
print(soup.select('head > title'))
print('查找p下面的id="link1"的标记')
print(soup.select('p > #link1'))
print('查找id="link1"之后class="sisiter"的所有兄弟节点')
print(soup.select('#link1 ~ .sister'))
print('查找紧跟id="link1"之后class="sister"的兄弟节点')
print(soup.select('#link1 + .sister'))

print('通过CSS的类名查找：')
print(soup.select('.sister'))
print(soup.select('[class~=sister]'))

print('通过tag的id查找：')
print(soup.select('#link1'))
print(soup.select('a#link1'))

print('通过是否存在某个属性连查找：')
print(soup.select('a[href]'))

print('通过属性值来查找：')
print(soup.select('a[href="http://example.com/elsie"]'))
print(soup.select('a[href^="http://"]'))
print(soup.select('a[href$="tillie"]'))
print(soup.select('[href*=".com/el"]'))
