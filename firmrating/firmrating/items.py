# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FirmratingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    order_num = scrapy.Field()
    bond_name = scrapy.Field()
    firm_rating = scrapy.Field()
    bond_rating = scrapy.Field()
    rating_exp = scrapy.Field()
    issue_time = scrapy.Field()
    rating_time = scrapy.Field()
