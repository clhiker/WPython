# 通过修改demo.py进行配置
# -*- coding: utf-8 -*-
import scrapy


class DemoSpider(scrapy.Spider):
    # 爬虫的名字，自定义
    name = 'demo'
    # 允许爬取内容在该域名以下
    #allowed_domains = ['python123.io']
    # scrapy爬取的初始页面列表

    start_urls = ['http://python123.io/ws/demo.html']

    # 用于处理响应，解析内容形成字典，发现新的URL爬取请求
    def parse(self, response):
        fname = response.url.split('/')[-1]
        with open(fname, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s.' % fname)

