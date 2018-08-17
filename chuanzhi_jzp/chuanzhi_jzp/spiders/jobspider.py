# -*- coding: UTF-8 -*-
import scrapy

from chuanzhi_jzp.items import ChuanzhiJzpItem

class ChuanzhiJzpSpider(scrapy.Spider):
    #spider名
    name = "jobspider"
    #创建域，允许作用的范围
    allowed_domains = ["http://www.itcast.cn/"]
    #爬虫起始的URL
    start_urls = ["http://www.itcast.cn/channel/teacher.shtml#"]


    def parse(self,response):
        #保存响应文件
        # with open("teach.html","w") as f: #用wb+ 要不然数据类型不对
        #     f.write(response.body) #xpath中的用法
        teacher_list = response.xpath('//div[@class="li_txt"]')
        #所有老师信息列表的集合，将数据追加到集合中
        # 遍历根节点集合
        # 加extract(),将匹配的结果转换为Unicode字符串
        # 不加extract()结果为xpath匹配的对象

        teacherItem = []

        for each in teacher_list:

            item = ChuanzhiJzpItem()

            name = each.xpath('./h3/text()').extract()
            # title
            title = each.xpath('./h4/text()').extract()
            # info
            info = each.xpath('./p/text()').extract()

            item['name'] = name[0]#若需要的话进行转码 先保存为记事本，然后另存为csv 保存类型为utf-8
            item['title'] = title[0]
            item['info'] = info[0]

            teacherItem.append(item) #【1】可以直接保存CSV

            # print(name) 在终端打印
            # print(title[0])
            # print(info[0])
            #将获取的数据交给pipelines
            yield item
        # return teacherItem #【1】可以直接保存CSV