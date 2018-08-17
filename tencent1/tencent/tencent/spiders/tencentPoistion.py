# -*- coding: utf-8 -*-
import scrapy

from tencent.items import TencentItem

class TencentpoistionSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['tencent.com']


    url =  'https://hr.tencent.com/position.php?&start='
    offset = 0

    start_urls = [url+str(offset)]


    def parse(self, response):
        for each in response.xpath("//tr[@class='even'] |//tr[@class='odd']"):
            #初始化模型对象
            item = TencentItem()
            # 职位名
            item["positionname"] = each.xpath("./td[1]/a/text()").extract_first()
            # 详情链接
            item["positionlink"] = each.xpath("./td[1]/a/@href").extract_first()
            # 职位类别
            item["positionType"] = each.xpath("./td[2]/text()").extract_first()
            # 招聘人数
            item["peopleNum"]    = each.xpath("./td[3]/text()").extract_first()
            # 工作地点
            item["worlLocation"] = each.xpath("./td[4]/text()").extract_first()
            # 发布时间
            item["publishTime"]  = each.xpath("./td[5]/text()").extract_first()

            yield item

        if self.offset < 60:
            self.offset += 10

        #自增10,每次处理完一页的数据之后，重新发送下一页的页面请求，重新拼接为新的URL,并调用self.pase，处理Response
        #将请求重新发送给调度器入队列，出队列，交给下载器下载
        yield scrapy.Request(self.url + str(self.offset),callback=self.parse)




