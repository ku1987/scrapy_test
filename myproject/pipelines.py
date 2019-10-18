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
    schema.drop_if_exists('dramas')
    # if not schema.has_table('dramas'):
    with schema.create('dramas') as table:
      table.increments('id')
      table.string('title')
      table.string('url')
      table.string('img')
      table.integer('year')
      table.string('tag')
      table.string('actor')
      table.string('director')
      table.long_text('detail')
      table.datetime('hulu_updated_date')
      table.boolean('hulu_flg').default(False)
      table.boolean('fod_flg').default(False)
      table.boolean('paravi_flg').default(False)
      table.boolean('tsutaya_tv_flg').default(False)
      table.boolean('amazon_prime_flg').default(False)
      table.boolean('dtv_flg').default(False)
      table.boolean('videopass_flg').default(False)
      table.boolean('rakuten_tv_flg').default(False)
      table.boolean('ranking_flg').default(False)

  def process_item(self, item, spider): 
    # タイトルで重複チェック
    is_exists = Drama.where('title', item['title']).get().pluck('id')

    if is_exists:
      is_exists = is_exists.get(0)
      target_sql = 'update'
    else:
      target_sql = 'insert'

    if target_sql == 'insert':
      dramas = Drama()
      dramas.hulu_updated_date = item['updated_at'] if 'updated_at' in item else datetime.datetime.today()
      dramas.title = item['title']
      dramas.url = item['url']
      dramas.img = item['img']
      dramas.year = item['year']
      dramas.tag = item['tag']
      dramas.actor = item['actor']
      dramas.director = item['director']
      dramas.detail = item['detail']
      dramas.hulu_flg = True
      dramas.save()

    elif target_sql == 'update':
      update_sql = {}
      update_sql['hulu_flg'] = True
      
      if 'tag' in item:
          update_sql['tag'] = item['tag']   
      if 'url' in item:
          update_sql['url'] = item['url']   
      if 'img' in item:
          update_sql['img'] = item['img']   
      if 'year' in item:
          update_sql['year'] = item['year'] 
      if 'detail' in item:
          update_sql['detail'] = item['detail']
      if 'actor' in item:
          update_sql['actor'] = item['actor']          
      if 'director' in item:
          update_sql['director'] = item['director']
      if 'detail' in item:
          update_sql['detail'] = item['detail']

      update_sql['hulu_updated_date'] = item['updated_at'] if 'updated_at' in item else datetime.datetime.today()
    
      #更新対象があればupdate
      if is_exists is not None:
          if update_sql.keys :
              Drama.where('id', int(is_exists)).update(update_sql)

