# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class ChuanzhiJzpPipeline(object):
    #初始化了一个文件，可选
    def __init__(self):
        self.filename = open('teacher.json','wb+')

    #必选方法，处理item数据的
    def process_item(self, item, spider):
        jsontext = json.dumps(dict(item),ensure_ascii=False) +"\n" #数据有中文时False
        self.filename.write(jsontext.encode("utf-8"))
        return item

    #可选方法，结束时调用
    def close_spdier(self,spider):
        self.filename.close()