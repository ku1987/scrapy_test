# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# import MySQLdb
from pymongo import MongoClient

class MongoPipeline:
    def open_spider(self, spider):
      self.client = MongoClient('localhost', 27017)
      self.db = self.client['hulu_drama']
      self.collection = self.db['items']

    def close_spider(self, spider):
      self.client.close()

    def process_item(self, item, spider):
      self.collection.insert_one(dict(item))
      return item

# class MySQLPipeline:
#   def open_spider(self, spider):
#     settings = spider.settings
#     params = {
#       'host':settings.get('MYSQL_HOST', 'localhost'),
#       'db': settings.get('MYSQL_DATABASE', 'scraping'),
#       'user': settings.get('MYSQL_USER', 'scraper'),
#       'passwd': settings.get('MYSQL_PASSWORD', 'password'),
#       'charset': settings.get('MYSQL_CHARSET', 'utf8mb4'),
#     }
#     self.conn = MySQLdb.connect(**params)
#     self.c = self.conn.cursor()

#     self.c.execute("""
#       create table if not exists `items` (
#         `id` integer not null auto_increment,
#         `title` varchar(200) not null,
#         primary key(`id`)
#       )
#     """)
#     self.conn.commit()

#   def close_spider(self, spider):
#     self.conn.close()

#   def process_item(self, item, spider):
#     self.c.execute('insert into `items` (`title`) values (%(title)s), dict(item)')
#     self.conn.commit()
#     return item