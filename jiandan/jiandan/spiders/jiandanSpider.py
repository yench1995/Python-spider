#!/usr/bin/env python
# encoding: utf-8

from scrapy.spiders import Spider
from jiandan.items import JiandanItem
from scrapy.http.request import Request

class JiandanSpider(Spider):
    name = 'jiandan'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }

    def start_requests(self):
        url = 'http://jandan.net/ooxx'
        yield Request(url, headers=self.headers)

    def parse(self, response):
        item = JiandanItem()
        item['image_urls'] = response.xpath('//img//@src').extract()
        yield item

        next_url = response.xpath('//a[@title="Older Comments"]/@href').extract()
        if next_url:
            yield Request(next_url[0], headers=self.headers)
