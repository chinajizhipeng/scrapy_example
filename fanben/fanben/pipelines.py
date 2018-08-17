# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class FanbenPipeline(object): #【不使用管道文件时可打开】
#     def process_item(self, item, spider):#【不使用管道文件时可打开】
#         return item #【不使用管道文件时可打开】

import json
class FanbenPipeline(object):
    #init方法时可选的，作为类的初始化方法
    def __init__(self):
        #创建了一个文件
        self.filename = open('teacher.json','w')  #写入json文件

    #处理item数据的，必须写

    def process_item(self, item, spider):
        jsontext = json.dumps(dict(item),ensure_ascii=False) #先将item转为字典，再将字典转换为json字符串 ,确认使用ascii编码
        self.filename.write(jsontext.encode('utf-8'))
        return item

    #可选的，结束时调用
    def close_spider(self,spider):
        self.filename.close()