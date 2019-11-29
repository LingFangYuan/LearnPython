import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# 初始化浏览器
options = webdriver.FirefoxOptions()
options.add_argument('-headless')
driver = webdriver.Firefox(options=options)
#driver = webdriver.Firefox()
driver.get('https://www.12306.cn/index/')

try:
    try:
        WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located((By.ID, 'page-loading'))
            )
    except Exception as e:
        print(e)
        driver.close()

    fromStationText = driver.find_element_by_id('fromStationText')
    toStationText = driver.find_element_by_id('toStationText')
    train_date = driver.find_element_by_id('train_date')
    search_one = driver.find_element_by_id('search_one')
    danChange = driver.find_element_by_id('danChange')

    js = 'document.getElementById("train_date").removeAttribute("readonly");'
    driver.execute_script(js)

    fromStationText.click()
    fromStationText.clear()
    fromStationText.send_keys('广州')
    panel_cities = driver.find_element_by_id('panel_cities').find_element_by_xpath('./div[span="广州"]')
    webdriver.ActionChains(driver).move_to_element(panel_cities).perform()
    panel_cities.click()
    time.sleep(1)

    toStationText.click()
    toStationText.clear()
    toStationText.send_keys('南雄')
    panel_cities = driver.find_element_by_id('panel_cities').find_element_by_xpath('./div[span="南雄"]')
    webdriver.ActionChains(driver).move_to_element(panel_cities).perform()
    panel_cities.click()
    time.sleep(1)

    train_date.clear()
    train_date.send_keys('2019-12-01')
    train_date.click()
    time.sleep(3)
    train_date.send_keys(Keys.SHIFT, Keys.TAB)
    toStationText.send_keys(Keys.TAB)
    date_button = driver.find_element_by_xpath('.//div[@class="cal-cm"]/div[@class="cell" and contains(@style, "border")]')
    date_button.click()


    search_one.click()

    driver.switch_to_window(driver.window_handles[1])
    print(driver.current_url)
    time.sleep(5)
    try:
        from_city = WebDriverWait(driver, 10).until(
            EC.visibility_of(driver.find_element_by_id('fromStationText'))
            )
    except Exception as e:
        print(e)
        raise
    toStationText = driver.find_element_by_id('toStationText')
    train_date = driver.find_element_by_id('train_date')

    print(from_city.get_attribute('value'), toStationText.get_attribute('value'), train_date.get_attribute('value'))
finally:
    driver.close()
