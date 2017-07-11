#!/usr/bin/env python
# encoding: utf-8

from scrapy.spiders import Spider
from douban.items import DoubanItem
from scrapy.http.request import Request

class DoubanSpider(Spider):
    name = 'douban_movie'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }

    def start_requests(self):
        url = 'https://movie.douban.com/top250'
        yield Request(url, headers=self.headers)

    def parse(self, response):
        item = DoubanItem()
        movies = response.xpath('//ol[@class="grid_view"]/li')
        for movie in movies:
            item['ranking'] = movie.xpath('.//div[@class="pic"]/em/text()').extract()
            item['movie_name'] = movie.xpath('.//div[@class="hd"]/a/span[1]/text()').extract()
            item['score'] = movie.xpath('.//div[@class="star"]/span[@class="rating_num"]/text()').extract()
            item['score_num'] = movie.xpath(
            './/div[@class="star"]/span/text()').re(ur'(\d+)人评价')
            yield item

        next_url = response.xpath('//span[@class="next"]/a/@href').extract()
        if next_url:
            next_url = 'https://movie.douban.com/top250' + next_url[0]
            yield Request(next_url, headers=self.headers)
