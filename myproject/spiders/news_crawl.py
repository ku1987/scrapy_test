# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from myproject.items import Headline

class NewsCrawlSpider(CrawlSpider):
    name = 'news_crawl'
    allowed_domains = ['news.yahoo.co.jp']
    start_urls = ['https://news.yahoo.co.jp/']

    rules = (
      Rule(LinkExtractor(allow=r'/pickup/\d+$'), callback='parse_topics'),
    )

    def parse_topics(self, response):
      """
      トピックスのページからタイトルと本文を抜き出す。
      """
      item = Headline()
      item['title'] = response.css('h2.tpcNews_title::text').get()
      item['body'] = response.css('p.tpcNews_summary::text').get()
      yield item
