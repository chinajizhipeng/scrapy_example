# -*- coding: utf-8 -*-
import scrapy


class ExamplesSpider(scrapy.Spider):
    name = 'examples'
    allowed_domains = ['http://blog.chacuo.net/']
    start_urls = ['http://quotes.toscrapy.com/']

    def parse(self, response):
        pass
