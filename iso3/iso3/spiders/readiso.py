# -*- coding: utf-8 -*-
import scrapy
from iso3.items import Iso3Item

class ReadisoSpider(scrapy.Spider):
    name = 'readiso'
    allowed_domains = ['blog.chacuo.net']
    start_urls = ['http://doc.chacuo.net/iso-3166-1']

    def parse(self, response):
        for tr in response.xpath('//tr'):
            item = Iso3Item()
            item['iso2'] = tr.xpath('td[1]/text()').extract_first()
            item['iso3'] = tr.xpath('td[2]/text()').extract_first()
            item['num'] = tr.xpath('td[3]/text()').extract_first()
            item['ENG_name'] = tr.xpath('td[5]/text()').extract_first()
            item['CHN_name'] = tr.xpath('td[6]/text()').extract_first()


            yield item