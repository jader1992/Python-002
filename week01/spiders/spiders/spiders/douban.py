import scrapy
from bs4 import BeautifulSoup
from scrapy import Selector
from spiders.items import DoubanMovieItem  # 选择器

class DobanSpider(scrapy.Spider):

    name = 'douban'
    allowed_domains = ['movie.douban.com']
    start_urls = ['http://movie.douban.com/top250/']

    # def parse(self, response):
    #     pass

    def start_requests(self):
        for i in range(0, 1):
            url = f'https://movie.douban.com/top250?start={i*25}'
            yield scrapy.Request(url=url, callback=self.parse, dont_filter=False)

    def parse(self, response):
        # items = []
        # soup = BeautifulSoup(response.text, 'html.parser')
        # title_list = soup.find_all('div', attrs={'class': 'hd'})

        # for i in title_list:
        #     item = DoubanMovieItem()
        #     title = i.find('a').find('span').text
        #     link = i.find('a').get('href')
        #     item['title'] = title
        #     item['link'] = link
        #     yield scrapy.Request(url=link, meta={'item': item}, callback=self.parse2)
        #     # items.append(item)

        # return items

        # print(response.text)
        movies = Selector(response= response).xpath('//div[@class="hd"]')

        for movie in movies:
            title = movie.xpath('./a/span/text()')
            link = movie.xpath('./a/@href')

            print('----------------------')
            print(title)
            print(link)
            print('----------------------')
            print(title.extract())
            print(link.extract())
            print(title.extract_first())
            print(link.extract_first())
            print(title.extract_first().strip())
            print(link.extract_first().strip())
            break




    def parse2(self, response):
        item = response.meta['item']
        soup = BeautifulSoup(response.text, 'html.parser')
        content = soup.find('div', attrs={'class': 'related-info'}).get_text().strip()
        item['content'] = content
        yield item  #返回pipline