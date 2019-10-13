# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import MySQLdb
# from pymongo import MongoClient

# class MongoPipeline:
#     def open_spider(self, spider):
#       self.client = MongoClient('localhost', 27017)
#       self.db = self.client['hulu_drama']
#       self.collection = self.db['items']

#     def close_spider(self, spider):
#       self.client.close()

#     def process_item(self, item, spider):
#       self.collection.insert_one(dict(item))
#       return item

class MySQLPipeline:
  def open_spider(self, spider):
    settings = spider.settings

    params = {
      'host':settings.get('MYSQL_HOST', 'scraping.cjxaqn9ex6dq.us-east-1.rds.amazonaws.com'),
      'db': settings.get('MYSQL_DATABASE', 'scraping'),
      'user': settings.get('MYSQL_USER', 'user'),
      'passwd': settings.get('MYSQL_PASSWORD', 'Dj2TFMe4f29zFbUxQsCM'),
      'charset': settings.get('MYSQL_CHARSET', 'utf8mb4'),
    }
    self.conn = MySQLdb.connect(**params)
    self.c = self.conn.cursor()

    self.c.execute('drop table if exists `dramas`')

    self.c.execute("""
      create table if not exists `dramas` (
        `id` integer not null auto_increment,
        `title` varchar(200) not null,        
        `year` int DEFAULT '1900' not null,
        `tag` varchar(255),
        `actor` varchar(255),
        `director` varchar(255),
        `detail` TEXT,
        primary key(`id`)
      )
    """)
    self.conn.commit()

  def close_spider(self, spider):
    self.conn.close()

  def process_item(self, item, spider):
    self.c.execute('''
                  insert into `dramas` (`title`,`year`,`tag`,`actor`,`director`,`detail`) 
                  values (%(title)s,%(year)s,%(tag)s,%(actor)s,%(director)s,%(detail)s)
                  ''',
                  dict(item))
    self.conn.commit()
    return item