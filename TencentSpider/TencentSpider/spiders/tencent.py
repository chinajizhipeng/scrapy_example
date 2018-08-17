# -*- coding: utf-8 -*-

#导入CrawlSpider类和Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from TencentSpider.items import TencentspiderItem
import scrapy

#导入链接规则匹配类，用来提取符合规则的链接
class TencentSpider(CrawlSpider):
    name = 'tencent'
    allowed_domains = ['hr.tencent.com'] #可以不写
    start_urls = ['http://hr.tencent.com/position.php?&start=0#a']
    #response里连接的提取规则，规定匹配规则,提取符合规则链接匹配对象的列表
    pagelink = LinkExtractor(allow=('strat=\d+'))
    # newlink = LinkExtractor(allow = ("123456"))
    #写rules规则,可以写多个链接
    rules = [
        #获取上一步列表里的链接，依次发送请求，并且依次继续跟进，调用指定的回调函数处理
        Rule(pagelink,callback="parse_item",follow=True)
        # Rule(newlink,callback="parse_item")
    ]
    #指定规定的回调函数
    def parse_item(self, response):
        print(response.rul)
        # i = {}
        for each in response.xpath("//tr[@class='even']"):
            item = TencentspiderItem()
            # 职位名
            item["positionname"] = each.xpath("td[1]/a/text()").extract()[0]
            # 详情链接
            item["positionlink"] = each.xpath("td[1]/a/@href").extract()[0]
            # 职位类别
            item["positionType"] = each.xpath("td[2]/text()").extract()[0]
            # 招聘人数
            item["peopleNum"] = each.xpath("td[3]/text()").extract()[0]
            # 工作地点
            item["worlLocation"] = each.xpath("td[4]/text()").extract()[0]
            # 发布时间
            item["publishTime"] = each.xpath("td[5]/text()").extract()[0]

            yield item
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        # return i
