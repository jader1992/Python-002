
from selenium import webdriver
import time

try:
    browser = webdriver.Chrome() #将会拉起我们的chrome浏览器

    browser.get('https://shimo.im/login?from=home') #接入我们的网址
    time.sleep(1)

    browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/input').send_keys('18042322550')
    browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/input').send_keys('12345678')
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/button').click()

    cookies = browser.get_cookies()
    time.sleep(3)

except Exception as e:
    print(e)
finally:
    browser.close()