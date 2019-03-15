# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import os
from scrapy.exporters import JsonLinesItemExporter

class XiaoshuoPipeline(object):
    #
    # def __init__(self):
    #     # self.fp = open('1.json', 'w', encoding='utf-8')
    #     self.path =
    #     self.fp =open('1.json','wb')
    #     self.exporter = JsonLinesItemExporter(self.fp,ensure_ascii =False,encoding = 'utf-8')

    def open_spider(self,spider):
        print("开始爬取")

    def process_item(self, item, spider):
        # line = json.dumps(dict(item), ensure_ascii=False)
        # self.fp.write(line)
        # self.exporter.export_item(item)
        # return item
        path = 'F:\data\\xiaoshuo'
        temppath = str(item["name"])
        targetpath = path + os.path.sep + temppath
        if not os.path.exists(targetpath):
            os.mkdir(targetpath)
        filename_path = targetpath + os.path.sep + str(item["chaptername"]) + '.txt'
        with open (filename_path ,'w',encoding='utf-8') as fp:
            fp.write(str(item["content"]))
            fp.close()
        return item

    def close_spider(self,spider):
        print('爬取结束')
