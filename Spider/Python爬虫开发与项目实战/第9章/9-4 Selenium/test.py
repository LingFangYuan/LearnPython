import time


from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox()
driver.get('http://www.baidu.com')
assert '百度' in driver.title
elem = driver.find_element_by_name('wd')
elem.clear()
elem.send_keys('网络爬虫')
elem.send_keys(Keys.RETURN)
time.sleep(3)
assert '网络爬虫.' not in driver.page_source
driver.close()
