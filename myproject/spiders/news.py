# -*- coding: utf-8 -*-
import scrapy
from myproject.items import Headline

class NewsSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['news.yahoo.co.jp']
    start_urls = ['https://news.yahoo.co.jp/']

    def parse(self, response):
      """
      トップページのトピックス一覧から個々のトピックスへのリンクを抜き出してたどる。
      """
      for url in response.css('ul.topicsList_main a::attr("href")').re(r'/pickup/\d+$'):
        yield response.follow(url, self.parse_topics)

    def parse_topics(self, response):
      """
      トピックスのページからタイトルと本文を抜き出す。
      """
      item = Headline()
      item['title'] = response.css('h2.tpcNews_title::text').get()
      item['body'] = response.css('p.tpcNews_summary::text').get()
      yield item
