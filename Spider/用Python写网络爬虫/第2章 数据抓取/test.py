import sys
import re
sys.path.append('..')

from 第1章网络爬虫简介.advanced_link_crawler import download


url = 'http://example.python-scraping.com/places/default/view/Afghanistan-1'
html = download(url)
print(re.findall(r'<td class="w2p_fw">(.*?)</td>', html)[1])
print(re.findall(r'<tr id="places_area__row"><td class="w2p_fl"><label class="readonly" for="places_area" id="places_area__label">Area: </label></td><td class="w2p_fw">(.*?)</td>', html))
print(re.findall(
    r'''<tr id="places_area__row">.*?<td\s*class=["']w2p_fw["']>(.*?)</td>''', html))

