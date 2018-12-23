# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from douban.items import DoubanItem


class DoumancomicscsSpider(CrawlSpider):
    name = "doubancomicsCS"
    allowed_domains = ["book.douban.com"]
    start_urls = ['https://book.douban.com/tag/漫画']
    
    rules = (
        Rule(LinkExtractor(allow = r'/tag/漫画',
                           restrict_xpaths = ('//*[@id="subject_list"]/div[2]/span/a')),
             callback = 'parse_item',
             follow = True),
             )
    
    def parse_item(self, response):
        for sel in response.xpath('//*[@id="subject_list"]/ul/li/div[2]'):
            item = DoubanItem()
            item['title'] = sel.xpath('h2/a/text()').extract_first()
            item['link'] = sel.xpath('h2/a/@href').extract_first()
            item['info'] = sel.xpath('div[1]/text()').extract_first()
            item['desc'] = sel.xpath('p/text()').extract_first()
            yield item
        
        