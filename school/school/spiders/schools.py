# -*- coding: utf-8 -*-
import scrapy
from school.items import SchoolItem

class SchoolsSpider(scrapy.Spider):
    name = 'schools'
    allowed_domains = ['news.qut.edu.cn']
    start_urls = ['http://news.qut.edu.cn/lgyw.htm']
    sss = []

    def parse(self, response):
        sss = []
        for each in response.xpath('//div[@class = main_conRCb1]//li'):
            item = SchoolItem()
            item['title'] = each.xpath('/a/text()').extract()
            item['time']  = each.xpath('/span/text()').extract()

            sss.append(item)

        return sss


