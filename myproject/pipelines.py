# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient

class MongoPipeline:
    def open_spider(self, spider):
      self.client = MongoClient('localhost', 27017)
      self.db = self.client['hulu_test']
      self.collection = self.db['items']

    def close_spider(self, spider):
      self.client.close()

    def process_item(self, item, spider):
      self.collection.insert_one(dict(item))
      return item
