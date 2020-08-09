from fake_useragent import UserAgent
ua = UserAgent(verify_ssl=False) #不要去进行ssl的验证

# print(f'Chrome浏览器：{ua.chrome}')
# print(ua.safari)

print(f'随机浏览器：{ua.random}')

