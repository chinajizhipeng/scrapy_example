# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs

class DongguanPipeline(object):
    def __init__(self):
        #这样就不用把每个数据都处理成UTF-8了
        self.filename = codecs.open("tencent.json","wb+",encoding='utf-8')


    def process_item(self, item, spider):
        #中文默认使用ascii码储存，禁用后默认为Unicode字符串
        text = json.dumps(dict(item),ensure_ascii=False)+'\n'
        self.filename.write(text)
        return item

    def close_spider(self,spider):
        self.filename.close()
