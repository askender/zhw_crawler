#!/usr/bin/python
#-*-coding:utf-8-*-

import traceback
from scrapy import log
from pymongo.connection import MongoClient
from zhw_crawler.settings import MONGODB_SERVER, MONGODB_NAME, MONGODB_PORT


class MongodbStorePipeline(object):

    def __init__(self):
        try:
            client = MongoClient(MONGODB_SERVER, MONGODB_PORT)
            self.db = client[self.MONGODB_NAME]
        except Exception as e:
            print("ERROR(MongodbStorePipeline): %s" % (str(e),))
            traceback.print_exc()

    @classmethod
    def from_crawler(cls, crawler):
        cls.MONGODB_SERVER = crawler.settings.get(
            'MONGODB_SERVER', 'localhost')
        cls.MONGODB_NAME = crawler.settings.get('MONGODB_NAME', 'test')
        cls.MONGODB_PORT = crawler.settings.getint('MONGODB_PORT', 27017)
        pipe = cls()
        pipe.crawler = crawler
        return pipe

    def process_item(self, item, spider):
        result = self.db[MONGODB_NAME].insert(dict(item))
        log.msg(
            "Item %s wrote to MongoDB database %s" % (result, MONGODB_NAME),
            level=log.DEBUG, spider=spider)
        return item
