from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()

    browser.get('https://movie.douban.com/subject/26871465/')
    time.sleep(1)

    btn1 = browser.find_element_by_xpath('//*[@id="comments-section"]/div[1]/h2/span/a')
    btn1.click()
    time.sleep(10)
    print(browser.page_source)
except Exception as e:
    print(e)
finally:
    browser.close()