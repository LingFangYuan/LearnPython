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

#soup = BeautifulSoup(html_str, 'lxml', from_encoding='utf-8')
soup = BeautifulSoup(open('index.html'), 'lxml', from_encoding='utf-8')
print(soup.p.get('class'), soup.p.attrs)
print(soup.p.string)
print(soup.a.string, type(soup.a.string))
print(soup.head.contents)
for child in soup.head.descendants:
    print(child)
print('$$$$$$$')
for parent in soup.a.parents:
    print(parent.name)
print('#############')
print(soup.p.next_sibling)
print(soup.p.prev_sibling)
print(soup.p.next_sibling.next_sibling)