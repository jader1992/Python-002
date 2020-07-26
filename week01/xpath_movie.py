
import requests
import lxml.etree
import pandas

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'

header = {"user-agent": user_agent}

movieUrl = 'https://movie.douban.com/subject/1292052/'

response = requests.get(movieUrl, headers=header)

# xml处理
selector = lxml.etree.HTML(response.text)

# 电影名称
filmName = selector.xpath('//*[@id="content"]/h1/span[1]/text()')
print(f'电影名称: {filmName}')

# 上映日期
planDate = selector.xpath('//*[@id="info"]/span[10]/text()')
print(f'上映日期: {planDate}')

# 评分
score = selector.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()')
print(f'评分: {score}')

movieList = [filmName, planDate, score]
print(movieList)

movieData = pandas.DataFrame(data = movieList)

movieData.to_csv('./movie.csv', encoding='utf-8', index=False, header=False)
