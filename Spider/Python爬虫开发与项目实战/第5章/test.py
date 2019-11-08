from lxml import etree


parser = etree.HTMLParser(encoding="utf-8")
htmlelement = etree.parse("temp.html", parser=parser)