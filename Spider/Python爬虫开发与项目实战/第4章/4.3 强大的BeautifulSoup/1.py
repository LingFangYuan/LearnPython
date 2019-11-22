import re

import bs4
from bs4 import BeautifulSoup



html_str = """
     <html><head><title>The Dormouse's story</title></head>
     <body>
     <p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
     <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
     <a href="http://example.com/lacie" class="sister" id="link2"><!-- Lacie --></a> and
     <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
     and they lived at the bottom of a well.</p>
     <p class="story">...</p>
     </body></html>
     """

#soup = BeautifulSoup(html_str, 'lxml')
soup = BeautifulSoup(open('index.html'), 'lxml')
print(soup.prettify())
print(soup.title)
print(soup.a)
print(soup.name, soup.attrs, soup.title.name)
print(soup.p.attrs, soup.p.get('class'), soup.p['class'])
if type(soup.a.string) != bs4.element.Comment:
    print(soup.a.string)

print('-' * 50)
print('遍历文档树:')
print('子节点：')
print(soup.head.contents)
print(len(soup.head.contents[0]), soup.head.contents[0].string)
for child in soup.head.children:
    print(child.string)
print('descendants:')
for child in soup.head.descendants:
    print(child)
for string in soup.stripped_strings:
    print(repr(string))

print('父节点：')
print(soup.title)
print(soup.title.parent)
print('所有父节点：')
print(soup.a)
for parent in soup.a.parents:
    if parent:
        print(parent.name)
    else:
        print(parent)
print('兄弟节点：')
print(soup.p.next_sibling)
print(soup.p.previous_sibling)
print(soup.p.next_sibling.next_sibling)
for sibling in soup.body.next_siblings:
    print(repr(sibling))
print('前后节点：')
print(soup.head)
print(soup.head.next_element)
print(soup.body.previous_element.previous_element)
for element in soup.a.next_elements:
    print(repr(element))
print('-' * 50)


print('搜索文档树：')
print('name参数:')
print(soup.find_all('b'))
print(soup.find_all(re.compile(r'^b')))
print(soup.find_all(['a', 'b']))
for tag in soup.find_all(True):
    print(tag.name)
def hasClass_Id(tag):
    return tag.has_attr('class') and tag.has_attr('id')
print(soup.find_all(hasClass_Id))

print('kwargs参数：')
print(soup.find_all(id='link2'))
print(soup.find_all(href=re.compile(r'elsie')))
print(soup.find_all(id=True))
print(soup.find_all('a', class_='sister'))
data_soup = BeautifulSoup('<div data-foo="value">foot!</div>', 'lxml')
print(data_soup.find_all(attrs={'data-foo': 'value'}))

print('text参数：')
print(soup.find_all(text='Tillie'))
print(soup.find_all(text=['Tillie', '...']))
print(soup.find_all(text=re.compile(r'Dormouse')))

print('limit参数：')
print(soup.find_all('a', limit=2))

print('recursive参数：')
print(soup.find_all('head'))
print(soup.find_all('head', recursive=False))
