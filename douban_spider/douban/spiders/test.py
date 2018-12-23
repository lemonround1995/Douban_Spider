# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

# 该爬虫用来测试rules中的规则对不对，是否爬到了所有页面
class TestSpider(CrawlSpider):
    name = "test"
    allowed_domains = ["book.douban.com"]
    start_urls = ['https://book.douban.com/tag/漫画']
    
    rules = (
        Rule(LinkExtractor(allow = r'/tag/漫画',
                           restrict_xpaths = ('//*[@id="subject_list"]/div[2]/span/a')),
             callback = 'parse_item',
             follow = True),
             )
    
    def parse_item(self, response):
        print(response.url)
