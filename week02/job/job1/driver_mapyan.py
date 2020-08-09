from selenium import webdriver
from selenium.webdriver import ActionChains
import time

try:
    browser = webdriver.Chrome() #将会拉起我们的chrome浏览器

    browser.get('https://maoyan.com/films?showType=3/') #接入我们的网址

    time.sleep(5)
    # browser.switch_to.frame(iframe)  # 切换到iframe
    btm1 = browser.find_element_by_id('yodaBox')

    action_chains = ActionChains(browser)
    action_chains.click_and_hold(btm1).perform()  # perform()用来执行ActionChains中存储的行为
    #
    action_chains.reset_actions()
    action_chains.move_by_offset(210, 0).perform()  # 移动滑块
    #
    # cookies = browser.get_cookies()
    # print(cookies)
    time.sleep(3)

except Exception as e:
    print(e)
finally:
    browser.close()