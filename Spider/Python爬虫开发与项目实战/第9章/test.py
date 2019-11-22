import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

# 初始化浏览器
options = webdriver.FirefoxOptions()
options.add_argument('-headless')
driver = webdriver.Firefox(options=options)
try:
    # driver.get('https://hotel.qunar.com/city/guangzhou/#fromDate=2019-11-23&bs=&bc=%E5%B9%BF%E5%B7%9E&QHFP=ZSL_A3AD1D22&cityurl=guangzhou&toDate=2019-11-25&from=hotellist')
    driver.get('http://hotel.qunar.com/')
    
    # 获取元素
    ele_toCity = driver.find_element_by_id('toCity')
    ele_fromDate = driver.find_element_by_id('fromDate')
    ele_toDate = driver.find_element_by_id('toDate')
    ele_search_btn = driver.find_element_by_class_name('search-btn')

    # 填入搜索信息
    # 填入城市
    ele_toCity.clear()
    ele_toCity.send_keys('广州')
    ele_toCity.click()

    # 填入入住日期
    ele_fromDate.clear()
    ele_fromDate.send_keys('2019-11-23')

    # 填入离开日期
    ele_toDate.clear()
    ele_toDate.send_keys('2019-11-25')

    # 点击搜索按钮
    ele_search_btn.click()
    num = 0
    while True:
        try:
            WebDriverWait(driver, 10).until(EC.title_contains('广州'))
        except Exception as e:
            print(e)
            break
        #time.sleep(5)


        # driver.find_element_by_tag_name('body').send_keys(Keys.END)
        # time.sleep(1)

        js = "window.scrollTo(0, document.body.scrollHeight);"
        driver.execute_script(js)

        time.sleep(5)
        html = driver.page_source
        num += 1
        print('第 %s 页成功' % num)

        try:
            next_page = WebDriverWait(driver, 10).until(
                EC.visibility_of(driver.find_element_by_css_selector('.item.next'))
            )
            next_page.click()
            time.sleep(5)
        except Exception as e:
            print(e)
            break
except Exception as e:
    print(e)
finally:
    driver.close()