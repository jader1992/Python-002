# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import os
import pandas
import csv

class MaoyanPipeline:

    def __init__(self):
        path = 'movie.csv'
        if os.path.exists(path):
            self.file = open(path, 'a+', encoding="utf-8", newline='')
            self.writer = csv.writer(self.file, dialect="excel")
        else:
            self.file = open(path, 'a+', encoding="utf-8", newline='')
            self.writer = csv.writer(self.file, dialect="excel")
            self.writer.writerow(['序号', '电影名称', '类型', '演员', '分数', '上映时间'])

    def process_item(self, item, spider):
        if item['name']:
            self.writer.writerow([item['order'], item['name'], item['type'], item['actor'], item['score'], item['time']])
        return item

    def close_spider(self, spider):
        self.file.close()
