# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from ..items import DoubanItem


class DoubancomicsSpider(scrapy.Spider):
    name = "doubancomics"
    allowed_domains = ["douban.com"]
    start_urls = ['https://book.douban.com/tag/%E6%BC%AB%E7%94%BB?start=0&type=T']

    def parse(self, response):
        for sel in response.xpath('//*[@id="subject_list"]/ul/li/div[2]'):
            item = DoubanItem()
            item['title'] = sel.xpath('h2/a/text()').extract_first()
            item['link'] = sel.xpath('h2/a/@href').extract_first()
            item['info'] = sel.xpath('div[1]/text()').extract_first()
            item['desc'] = sel.xpath('p/text()').extract_first()
            yield item
        
        # 爬行多页
        next_page_1 = response.xpath('//*[@id="subject_list"]/div[2]/span[4]/a/@href').extract_first()
        # 因为“后页”的格式有变
        next_page_2 = response.xpath('//*[@id="subject_list"]/div[2]/span[5]/a/@href').extract_first()
        if next_page_1:
            url = u'https://book.douban.com' + next_page_1
            yield Request(url, callback=self.parse)
        if next_page_2:
            url = u'https://book.douban.com' + next_page_2
            yield Request(url, callback=self.parse)