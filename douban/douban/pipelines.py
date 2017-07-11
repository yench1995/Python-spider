# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
import sys

reload(sys)
sys.setdefaultencoding('utf8')

class DoubanPipeline(object):
    def __init__(self):
        self.file = codecs.open('douban_movie.json', mode='wb', encoding='utf-8')

    def process_item(self, item, spider):
        line = 'the new move list:'+'\n'

        for i in range(len(item['ranking'])):
            ranking = {'ranking':item['ranking'][i]}
            score = {'socre':item['score'][i]}
            movie_name = {'movie_name':str(item['movie_name'][i])}
            score_num = {'score_num':item['score_num'][i]}
            line = line + json.dumps(ranking, ensure_ascii=False)
            line = line + json.dumps(score, ensure_ascii=False)
            line = line + json.dumps(movie_name, ensure_ascii=False)
            line = line + json.dumps(score_num, ensure_ascii=False) + '\n'

        self.file.write(line)

    def close_spider(self, spider):
        self.file.close()
