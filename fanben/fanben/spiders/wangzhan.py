# -*- coding: utf-8 -*-
import scrapy
from fanben.items import ItcastItem #将爬取的内容导进Items文件
#创建一个爬虫类
class WangzhanSpider(scrapy.Spider):
    # 创建爬虫名字，执行的名字
    name = 'wangzhan'
    # 允许爬虫的范围
    allowed_domains = ['itcast.cn']
    #设置爬取原始URL的地址
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml#'] #也可用元组，加逗号

    def parse(self, response):

        # 将url内容下载到本地
        # with open('teacher.html','wb+') as f:
        #     f.write(response.body)

        # 通过scrapy自带的xpath匹配出所有的老师的节点
        teacher_list = response.xpath('//div[@class="li_txt"]')

        #所有老师信息列表的集合，将数据追加到集合中
        # teacherItem = [] #【1】一并返回列表
        # 遍历根节点集合
        for each in teacher_list:
            #Item对象用来保存数据的
            item = ItcastItem()
            # name,
            # 加extract(),将匹配的结果转换为Unicode字符串
            # 不加extract()结果为xpath匹配的对象
            name = each.xpath('./h3/text()').extract()
            # title
            title = each.xpath('./h4/text()').extract()
            # info
            info = each.xpath('./p/text()').extract()
            # print(name[0])
            # print(title[0])
            # print(info[0])
            item['name'] = name[0]
            item['title'] = title[0]
            item['info'] = info[0]

            

            # teacherItem.append(item)  #【1】一并返回列表
        return teacherItem #【1】一并返回列表 不使用管道文件时实际用
