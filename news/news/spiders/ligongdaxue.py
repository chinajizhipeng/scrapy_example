# -*- coding: utf-8 -*-

import scrapy
from news.items import NewsItem

class LigongdaxueSpider(scrapy.Spider):

    name = 'ligongdaxue'
    allowed_domains = ['news.qut.edu.cn']


    url = 'http://news.qut.edu.cn/lgyw/'
    offset = 352
    start_urls = [url+str(offset)+'.htm']
    # start_urls = ['http://news.qut.edu.cn/lgyw/352.htm']
    def parse(self, response):

        news_list = response.xpath('//div[@class="main_conRCb1"]/ul/li')


        for new in news_list:

            item = NewsItem()

            item['title'] = new.xpath('./a/text()').extract_first()
            item['url']   = "http://news.qut.edu.cn"+new.xpath('./a/@href').extract_first()[2:]
            item['time']  = new.xpath('./span/text()').extract_first()

            yield item

        if self.offset > 0:
            self.offset -= 1


        yield scrapy.Request(self.url+str(self.offset)+'.htm',callback=self.parse)

