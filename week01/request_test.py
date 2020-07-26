
import requests

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'

header = {"user-agent": user_agent}

movieUrl = 'https://movie.douban.com/top250'

response = requests.get(movieUrl, headers=header)

print(response.text)
print(f'返回码：{response.status_code}')
