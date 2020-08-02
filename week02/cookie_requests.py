from fake_useragent import UserAgent
import requests

ua = UserAgent(verify_ssl=False)
headers = {
    "User-Agent": ua.random,
    "Referer": "https://accounts.douban.com/passport/login_popup?login_source=anony"
}

s = requests.Session()

login_url = 'https://accounts.douban.com/j/mobile/login/basic'
form_data = {
    'ck':'',
    'name':'15055495@qq.com',
    'password':'',
    'remember':'false',
    'ticket':''
}

response = s.post(url=login_url, data=form_data, headers=headers)
print(response.text)
# post数据前获取cookie
# pre_login = ""