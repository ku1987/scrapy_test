# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

# class Headline(scrapy.Item):
#   title = scrapy.Field()
#   body = scrapy.Field()

# class Restaurant(scrapy.Item):
#   name = scrapy.Field()
#   address = scrapy.Field()
#   latitude = scrapy.Field()
#   longtitude = scrapy.Field()
#   station= scrapy.Field()
#   score = scrapy.Field()

class Hulu(scrapy.Item):
  title = scrapy.Field()
  tag = scrapy.Field()
  year = scrapy.Field()
  detail = scrapy.Field()
  actor = scrapy.Field()
  director = scrapy.Field()