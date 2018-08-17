# -*- coding: utf-8 -*-
import scrapy
from firmrating.items import FirmratingItem

class FinSpider(scrapy.Spider):
    name = 'fin'
    allowed_domains = ['www.ccxi.com.cn']

    #设定爬取网页
    url = "http://www.ccxi.com.cn/cn/Init/bond/310/0?&page=1"
    offset = 1
    start_urls = [url+str(offset)]

    # start_urls = ["http://www.ccxi.com.cn/cn/Init/bond/310/0?&page=1"]

    #start_urls = [http://www.ccxi.com.cn/cn/Init/bond/310/0?&page=1]

    def parse(self, response):
        print(response.url)
        for rating in response.xpath('//table[@class="show-lg"]/tbody/tr'):

            item = FirmratingItem()

            item["order_num"] = rating.xpath("td[1]/text()").extract_first()
            item["bond_name"] = rating.xpath("td[2]/a/text()").extract_first()
            item["firm_rating"] = rating.xpath("td[3]/text()").extract_first()
            item["bond_rating"] = rating.xpath("td[4]/text()").extract_first()
            item["rating_exp"] = rating.xpath("td[5]/text()").extract_first()
            item["issue_time"] = rating.xpath("td[6]/text()").extract_first()
            item["rating_time"] = rating.xpath("td[7]/text()").extract_first()

            yield item

        if self.offset < 244:
            self.offset += 1

        yield scrapy.Request(self.url + str(self.offset)+'.htm',callback=self.parse)

