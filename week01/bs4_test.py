
import requests
from bs4 import BeautifulSoup as bs

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'

header = {"user-agent": user_agent}

movieUrl = 'https://movie.douban.com/top250'

response = requests.get(movieUrl, headers=header)

bs_info = bs(response.text, 'html.parser')

for tags in bs_info.find_all('div', attrs={'class': 'hd'}):
    for atag in tags.find_all('a'):
        # 获取所有连接
        print(atag.get('href'))
        # 获取所有电影名字
        print(atag.find('span').text)


