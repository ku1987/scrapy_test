# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from myproject.items import Restaurant

class TabeolglSpider(CrawlSpider):
    name = 'tabelog'
    allowed_domains = ['tabelog.com']
    start_urls = ['https://tabelog.com/tokyo/rstLst/lunch/?RdoCosTp=1&LstCosT=2']

    rules = [
      Rule(LinkExtractor(allow=r'/\w+/rstLst/lunch/\d/')),
      Rule(LinkExtractor(allow=r'/\w+/A\d+/A\d+/\d+/$'),
       callback='parse_response'),
    ]

    def parse_response(self, response):
      """
      トピックスのページからタイトルと本文を抜き出す。
      """
      item = Restaurant(
        name = response.css('.display-name').xpath('string()').get().strip(),
        address = response.css('.rstinfo-table__address').xpath('string()').get().strip(),
        station = response.css('dt:contains("最寄り駅")+dd span::text').get(),
        score = response.css('[rel="v:rating"] span::text').get(),
      )
      yield item
