# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from douban.items import DoubanItem


class ImagespiderSpider(CrawlSpider):
    name = "imagespider"
    allowed_domains = ["book.douban.com"]
    start_urls = ['https://book.douban.com/tag/漫画']
    
    rules = (
        Rule(LinkExtractor(allow = r'/tag/漫画',
                           restrict_xpaths = ('//*[@id="subject_list"]/div[2]/span/a')),
             callback = 'parse_item',
             follow = True),
             )

    def parse_item(self, response):
        item = DoubanItem()
        for img in response.xpath('//*[@id="subject_list"]/ul/li/div[1]'):
            item['image_urls'] = img.xpath('a/img/@src').extract()
            yield item
