# -*- coding: utf-8 -*-
import scrapy
import re
from xiaoshuo.items import XiaoshuoItem
import  re

class XiaoshuospiderSpider(scrapy.Spider):
    name = 'xiaoshuospider'
    allowed_domains = ['23us.com']
    start_urls = ['https://www.23us.so/list/1_1.html']

    def parse(self, response):
        urls = response.xpath("//table//td[@class='L']/a[@target='_blank']/@href").getall()
        for url in urls:
            yield  scrapy.Request(url,callback=self.get_curl,dont_filter=True)

    def get_curl(self,response):
        name = response.xpath("//div[@class='bdsub']//dd/h1/text()").get()
        name = re.sub("最新章节",'',name)
        chapters_url = response.xpath("//table//td/a/@href").getall()
        for chapter_url in chapters_url:
            yield  scrapy.Request(chapter_url,callback=self.get_page,dont_filter=True,meta={"name":name})

    def get_page(self,response):
        chapter_name = response.xpath("//div[@class='bdsub']//dd/h1/text()").get()
        contents = response.xpath("//div[@class='bdsub']//dd[@id='contents']/text()").getall()
        contents = "".join(contents).strip("\r").split()
        item = XiaoshuoItem()
        item["name"] = str(response.meta["name"])
        item["chaptername"] = chapter_name
        item["content"]  = contents
        yield item

