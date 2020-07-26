
import requests
from bs4 import BeautifulSoup as bs
import pandas
import numpy
import re
import time


movieUrl = 'https://maoyan.com/films?showType=3'
userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
cookie = 'uuid_n_v=v1; uuid=623213C0CF4A11EA9D9027CAB3F025F8A1814158FA1742E5B48F549EDC7F0900; _csrf=a83958c5fe77e1aa5569d63f33e8fab6503fb91797c2c915f11e62b73e5593e2; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1595772898; _lxsdk_cuid=1738b7a0c734d-0e015a05a9adb7-31617402-1fa400-1738b7a0c7441; _lxsdk=623213C0CF4A11EA9D9027CAB3F025F8A1814158FA1742E5B48F549EDC7F0900; mojo-uuid=dfd55e56875b91c9105e6b7438ad37ea; mojo-session-id={"id":"daa4a2016fc47815eef63c125b1c3aaf","time":1595772898493}; mojo-trace-id=2; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1595772905; __mta=46947736.1595772898549.1595772898549.1595772905206.2; _lxsdk_s=1738b7a0c77-abf-dc1-7aa%7C%7C4'

fetchMovieTitle = []
fetchMovieUrl = []
fetchMovieDate = []
fetchMovieType = []

def getList(myurl, cookie, userAgent):

    baseUrl = 'https://maoyan.com'
    header = {
        "cookie": cookie,
        "User-Agent": userAgent
    }


    response = requests.get(myurl, headers=header)
    bs_info = bs(response.text, 'html.parser')

    data = []
    tags = bs_info.find_all('div', attrs={'class': 'channel-detail movie-item-title'})

    for i in range(0,10):
        atag = tags[i]
        film = atag.text
        href = atag.find('a').get('href')
        if href is None:
            continue
        else :
            href = baseUrl + href
        fetchMovieTitle.append(film.strip())
        fetchMovieUrl.append(href)
        # movieDetail = getDetail(href, userAgent, detailCookie)
        # data.append(film.strip())
        # data.append(movieDetail[0].strip())
        # data.append(movieDetail[1].strip())
    # output(data)

def getDetail(url, cookie, userAgent):

    header = {
        "cookie": cookie,
        "User-Agent": userAgent
    }
    response = requests.get(url, headers=header)
    bs_info = bs(response.text, 'html.parser')
    movieTypes = bs_info.find_all('a', attrs={'class': 'text-link'})
    ellipsis = list(bs_info.find_all('li', attrs={'class': 'ellipsis'}))
    showTime = ellipsis[-1].text
    type = []
    for movie in movieTypes:
        type.append(movie.text.strip())
    fetchMovieDate.append(showTime.strip())
    fetchMovieType.append(','.join(type))


def output(data):
    movieData = pandas.DataFrame(data=data)
    movieData.to_csv('./movie.csv', encoding='utf-8', index=False, header=False, sep=' ')

#抓取电影名称，电影链接
getList(movieUrl, userAgent, cookie)
time.sleep(2)

# 获取电影类型，上映时间
detailCookie = '__mta=46947736.1595772898549.1595773510801.1595775004065.5; uuid_n_v=v1; uuid=623213C0CF4A11EA9D9027CAB3F025F8A1814158FA1742E5B48F549EDC7F0900; _csrf=a83958c5fe77e1aa5569d63f33e8fab6503fb91797c2c915f11e62b73e5593e2; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1595772898; _lxsdk_cuid=1738b7a0c734d-0e015a05a9adb7-31617402-1fa400-1738b7a0c7441; _lxsdk=623213C0CF4A11EA9D9027CAB3F025F8A1814158FA1742E5B48F549EDC7F0900; mojo-uuid=dfd55e56875b91c9105e6b7438ad37ea; __mta=46947736.1595772898549.1595772905206.1595772915865.3; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1595775004; _lxsdk_s=1738c397732-293-494-a97%7C%7C1'
for url in fetchMovieUrl:
    getDetail(url, detailCookie, userAgent)

data = [fetchMovieDate,fetchMovieType,fetchMovieTitle]
data = (numpy.rot90(data,-1)).tolist()
output(data)