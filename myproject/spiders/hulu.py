# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from myproject.items import Hulu
from ..settings import START_URLS
from ..selenium_middleware import close_driver

import re

class HuluSpider(CrawlSpider):
    name = 'hulu'
    allowed_domains = ['www.hulu.jp','hulu.jp']
    start_urls = START_URLS    

    def parse(self, response):
      
      for url in response.css('.vod-mod-tile__item > a::attr("href")'):
        yield response.follow(url, self.parse_response)

    def parse_response(self, response):
      year_str = response.css('.vod-mod-detail-info02__copyright small').xpath('string()').get()

      array_tag = response.css('ul.vod-mod-detail-info02__genre > li').xpath('string()').extract()
      array_actor = response.css('.vod-mod-detail-info02__credit-row:first-child .vod-mod-detail-info02__credit-col:nth-child(1) ul li').xpath('string()').extract()
      array_director = response.css('.vod-mod-detail-info02__credit-col:nth-child(2) ul li').xpath('string()').extract()
        
      item = Hulu(
        title = response.css('.vod-mod-detail-info02__title').xpath('string()').get().strip(),  
        tag = ', '.join(array_tag),        
        year = int(re.findall(r'[0-9]{4}', year_str)[0]),
        actor = ', '.join(array_actor),
        director = ', '.join(array_director),
        detail = response.css('.vod-mod-detail-info02__program-description p').xpath('string()').get()
      )
      yield item

    def closed(self, reason):
      close_driver()
