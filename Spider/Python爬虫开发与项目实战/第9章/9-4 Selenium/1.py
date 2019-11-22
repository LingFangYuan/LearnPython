import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


driver = webdriver.Firefox()
driver.get('file:///F:/GitRepository/Learning/Spider/Python%E7%88%AC%E8%99%AB%E5%BC%80%E5%8F%91%E4%B8%8E%E9%A1%B9%E7%9B%AE%E5%AE%9E%E6%88%98/%E7%AC%AC9%E7%AB%A0/9-4%20Selenium/login.html')

username = driver.find_element_by_name('username')
password = driver.find_element_by_xpath('.//*[@id="loginForm"]/input[2]')
login_button = driver.find_element_by_xpath('.//input[@type="submit"]')

username.send_keys('ling')
password.send_keys('3sdfeg')
login_button.click()

select = driver.find_element_by_xpath('//form/select')
all_option = select.find_elements_by_tag_name('option')
for option in all_option:
    print('Value is： %s' % option.get_attribute('value'))
    option.click()

select = Select(driver.find_element_by_xpath('//form/select'))
select.select_by_index(0)
time.sleep(2)
select.select_by_visible_text('手机号')
time.sleep(2)
select.select_by_value('name')


