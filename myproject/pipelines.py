# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import MySQLdb
import datetime

from orator import DatabaseManager, Model
from orator import Schema

config = {
    'mysql': {
        'driver': 'mysql',
        'host': 'localhost',
        'database': 'hulu_test',
        'user': 'user',
        'password': 'user',
        'prefix': ''
    }
}

db = DatabaseManager(config)
schema = Schema(db)

Model.set_connection_resolver(db)

class Drama(Model):
    __table__ = 'dramas'
    __timestamps__ = False

class MySQLPipeline:
  def open_spider(self, spider):
    if not schema.has_table('dramas'):
      with schema.create('dramas') as table:
        table.increments('id')
        table.string('title')
        table.integer('year')
        table.string('tag')
        table.string('actor')
        table.string('director')
        table.string('detail')
    # settings = spider.settings

    # params = {
    #   'host':settings.get('MYSQL_HOST', 'localhost'),
    #   # scraping.cjxaqn9ex6dq.us-east-1.rds.amazonaws.com
    #   'db': settings.get('MYSQL_DATABASE', 'hulu_test'),
    #   'user': settings.get('MYSQL_USER', 'user'),
    #   'passwd': settings.get('MYSQL_PASSWORD', 'user'),
    #   'charset': settings.get('MYSQL_CHARSET', 'utf8mb4'),
    # }
    # self.conn = MySQLdb.connect(**params)
    # self.c = self.conn.cursor()

    # self.c.execute("""
    #   create table if not exists `dramas` (
    #     `id` integer not null auto_increment,
    #     `title` varchar(255) not null,
    #     `year` int DEFAULT '1900' not null,
    #     `tag` varchar(255),
    #     `actor` varchar(255),
    #     `director` varchar(255),
    #     `detail` TEXT,
    #     primary key(`id`)
    #   )
    # """)
    # self.conn.commit()

  # def close_spider(self, spider):
  #   self.conn.close()

  def process_item(self, item, spider):
    # self.c.execute('''
    #               insert into `dramas` (`title`,`year`,`tag`,`actor`,`director`,`detail`) 
    #               values (%(title)s,%(year)s,%(tag)s,%(actor)s,%(director)s,%(detail)s)
    #               ''',
    #               dict(item))
    # self.conn.commit()
    dramas = Drama()
    dramas.title = item['title']
    dramas.year = item['year']
    dramas.tag = item['tag']
    dramas.actor = item['actor']
    dramas.director = item['director']
    dramas.detail = item['detail']
    dramas.save()
