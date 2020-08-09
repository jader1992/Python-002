# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import os
import pandas
import csv
import re
import pymysql

class MaoyanPipeline:

    def __init__(self, dbInfo):
        self.host = dbInfo['host']
        self.port = dbInfo['port']
        self.user = dbInfo['user']
        self.password = dbInfo['password']
        self.db = dbInfo['db']

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            dbInfo=crawler.settings.get("DBINFO")
        )

    def open_spider(self, spider):
        self.conn = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.db
        )
        self.cur = self.conn.cursor()

    def process_item(self, item, spider):
        if item['name']:
            name = item['name']
            type1 = item['type']
            actor = item['actor']
            score = item['score'] if item['score'] != '' else 0.0
            time = item['time']

            try:
                query = "insert into `movie` (`title`, `type`, `actor`, `score`, `date`) values (%s, %s, %s, %s, %s)"
                values = (name, type1, actor, score, time)
                self.cur.execute(query, values)
                self.conn.commit()
            except Exception as e:
                self.conn.rollback()

        return item

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()
