
from urllib import request
from http import cookiejar

url = 'http://httpbin.org/get'

# GET 方法
resp = request.urlopen(url)
print(resp.read().decode())

# POST 方法
# resp = request.urlopen(url, data=b'key=value', timeout=10)
# print(resp.read().decode())

# cookie

# 创建一个cookiejar对象
cookie = cookiejar.CookieJar()

# 创建cookie处理器
handler = request.HTTPCookieProcessor(cookie)

# 创建opener对象
opener = request.build_opener(handler)

# 使用opener来发起请求
resp = opener.open('http://www.baidu.com')

for i in cookie:
    print(i)
