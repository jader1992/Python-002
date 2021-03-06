import scrapy
import csv
from bs4 import BeautifulSoup
from scrapy.selector import Selector
from maoyan.items import MaoyanItem

class FetchmovieSpider(scrapy.Spider):
    name = 'fetchmovie'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3/']

    def start_requests(self):
        url = 'https://maoyan.com/films?showType=3'
        yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        # print(response.text)
        # soup = BeautifulSoup(response.text, 'html.parser')
        # print(soup)

        # movies = Selector(response=response).xpath('//div[@class="movie-hover-info"]')

        movies = Selector(response).xpath('//div[@class="movie-hover-info"]')[0:10]
        i = 1
        for movie in movies:
            item = MaoyanItem()
            # print(movie.xpath('./div[1]/span[1]/text()').extract_first())
            item['order'] = i
            item['name'] = movie.xpath('./div[1]/span[1]/text()').extract_first()

            intergerScore = movie.xpath('./div[1]/span[2]/i[1]/text()').extract_first()
            if intergerScore is None:
                intergerScore = ''
            else:
                intergerScore = str(intergerScore)
            floatScore = movie.xpath('./div[1]/span[2]/i[2]/text()').extract_first()
            if floatScore is None:
                floatScore = ''
            else:
                floatScore = str(floatScore)
            score = intergerScore + floatScore
            item['score'] = score
            item['type'] = movie.xpath('./div[2]/text()').extract()[1].strip()
            item['actor'] = movie.xpath('./div[3]/text()').extract()[1].strip()
            item['time'] = movie.xpath('./div[4]/text()').extract()[1].strip()
            i += 1
            yield item
