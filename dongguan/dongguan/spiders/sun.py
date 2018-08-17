# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from dongguan.items import DongguanItem
import re

class SunSpider(CrawlSpider):
    name = 'sun'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=0']

    rules = (
        Rule(LinkExtractor(allow=r'type=4&page=\d+')),
        Rule(LinkExtractor(allow=r'/html/question/\d+/\d+.shtml'),callback="parse_item")
    )

    # rules2 = (
    #     Rule(LinkExtractor(allow=r'type=4')，process_links='deal_links',callback='parse_item'),
    # )
    #需要重新处理每个response里提取的链接，Type&page=xxx?type=4修改为Type?page=xxx&type=4
    #Links就是LinkExtractor提取的链接
    def deal_links(self,links):
        for link in links:
            link.url.replace('?','&').replace('Type&','Type?')
        #返回修改完的links链接列表
        return links

    def parse_item(self, response):
        # i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        item = DongguanItem()
        # 网站
        item['url'] = response.url
        # 标题
        item['title'] = response.xpath('//div[@class = "pagecenter p3"]//strong/text()').extract()[0]
        # 编号
        item['num'] = item['title'].split(' ')[-1].split(":")[-1]
        # 内容,先使用取出有图片的情况下的匹配规则，如果有内容,返回所有内容的列表集合
        content = response.xpath('//div[@class="contentext"]/text()').extract()
        #如果没有内容返回空列表，则使用无图片情况下的匹配规则
        if len(content) == 0:
            content= response.xpath('//div[@class="c1 text14_2"]/text()').extract()
            item['content'] = "".join(content).strip()
        else:
            item['content'] = "".join(content).strip()

        yield item

