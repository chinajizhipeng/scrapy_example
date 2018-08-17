# -*- coding: UTF-8 -*-
from scrapy.loader.processors import MapCompose, Join
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
from scrapy.http import FormRequest
from login_firmrating import items

class LoginSpider(CrawlSpider):
    name = 'login'

    def start_requests(self):
        return [
            FormRequest(
                "http://www.ccxi.com.cn/cn/Login/doLogin",
                formdata={"name": "chinajzp", "password": "Woaini0901"}
            )]