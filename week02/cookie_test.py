import requests

# 在同一个 Session 实例发出的所有请求之间保持 cookie
session = requests.session()

session.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
r = session.get('http://httpbin.org/cookies')

print(r.text)
# '{"cookies": {"sessioncookie": "123456789"}}'

# 会话可以使用上下文管理器
with requests.Session() as s:
    r1 = s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
    print(r1.text)
