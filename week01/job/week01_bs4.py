
import requests
from bs4 import BeautifulSoup as bs
import pandas
import re

movieUrl = 'https://maoyan.com/films?showType=3'
userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
cookie = '__mta=46947736.1595772898549.1596004106629.1596163789775.8; uuid_n_v=v1; uuid=623213C0CF4A11EA9D9027CAB3F025F8A1814158FA1742E5B48F549EDC7F0900; _csrf=a83958c5fe77e1aa5569d63f33e8fab6503fb91797c2c915f11e62b73e5593e2; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1595772898; _lxsdk_cuid=1738b7a0c734d-0e015a05a9adb7-31617402-1fa400-1738b7a0c7441; _lxsdk=623213C0CF4A11EA9D9027CAB3F025F8A1814158FA1742E5B48F549EDC7F0900; mojo-uuid=dfd55e56875b91c9105e6b7438ad37ea; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1596206370; __mta=46947736.1595772898549.1596163789775.1596206370570.9; _lxsdk_s=173a56d5c3b-40-6f2-88f%7C%7C1'
movieList = []

def getList(myurl, cookie, userAgent):

    header = {
        "cookie": cookie,
        "User-Agent": userAgent
    }
    response = requests.get(myurl, headers=header)
    bs_info = bs(response.text, 'html.parser')

    tags = bs_info.find_all('div', attrs={'class': 'movie-hover-info'})
    if len(tags) == 0:
        return movieList

    i , movieData = 0, []
    for tag in tags:
        if i > 9:
            break
        else :
            i += 1
            movieName = tag.find('span', attrs={'class': 'name'}).get_text()
            scoreInt = tag.find('i', attrs={'class': "integer"})
            if scoreInt is None:
                scoreInt = ''
            else:
                scoreInt = scoreInt.get_text()
            scoreFraction = tag.find('i', attrs={'class': 'fraction'})
            if scoreFraction is None:
                scoreFraction = ''
            else :
                scoreFraction = scoreFraction.get_text()
            movieScore = scoreInt + scoreFraction
            movieType = re.sub('类型:', '', tag.find_all('div', attrs={'class': 'movie-hover-title'})[1].text).strip()
            movieActor = re.sub('主演:', '', tag.find_all('div', attrs={'class': 'movie-hover-title'})[2].text).strip()
            movieTime = re.sub('上映时间:', '', tag.find_all('div', attrs={'class': 'movie-hover-title'})[3].text).strip()
            movieData.append([i, movieName, movieType, movieActor, movieScore, movieTime])

    return movieData

if __name__ == "__main__":
    movieData = getList(movieUrl, cookie, userAgent)
    if len(movieData) == 0:
        print("There is no data need output")
    else :
        movieData = pandas.DataFrame(data=movieData)
        movieData.to_csv('./movie.csv', encoding='utf-8',  header=['序号', '电影名称', '电影类型', '电影主演', '电影分数', '上映时间'], index=False, sep=',')
        print("data is output")
