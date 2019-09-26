# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from myproject.items import Hulu
from ..settings import START_URLS
from ..selenium_middleware import close_driver

class HuluSpider(CrawlSpider):
    name = 'hulu'
    allowed_domains = ['www.hulu.jp','hulu.jp']
    start_urls = START_URLS    

    def parse(self, response):
      
      for url in response.css('.vod-mod-tile__item > a::attr("href")'):
        yield response.follow(url, self.parse_response)

    def parse_response(self, response):
      """
      トピックスのページからタイトルと本文を抜き出す。
      """
      item = Hulu(
        title = response.css('.vod-mod-detail-info02__title').xpath('string()').get().strip(),
        tag = response.css('ul.vod-mod-detail-info02__genre > li:first-child').xpath('string()').get().strip(),
        year = response.css('.vod-mod-detail-info02__copyright small').xpath('string()').get(),
        detail = response.css('.vod-mod-detail-info02__program-description p').xpath('string()').get(),
      )
      yield item

    def closed(self, reason):
      close_driver()
