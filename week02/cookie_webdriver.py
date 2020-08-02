from selenium import webdriver
import time

try:
    browser = webdriver.Chrome() #将会拉起我们的chrome浏览器

    browser.get('https://www.douban.com') #接入我们的网址
    time.sleep(1)

    browser.switch_to.frame(browser.find_elements_by_tag_name('iframe')[0])
    btm1 = browser.find_element_by_xpath('/html/body/div[1]/div[1]/ul[1]/li[2]')
    btm1.click()
    time.sleep(1)

    browser.find_element_by_xpath('//*[@id="username"]').send_keys('1249200310@qq.com')
    browser.find_element_by_id('password').send_keys('hkjlkjnkljn')
    time.sleep(1)
    browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[5]/a').click()

    cookies = browser.get_cookies()
    print(cookies)
    time.sleep(3)

except Exception as e:
    print(e)
finally:
    browser.close()