#! /usr/bin/env python
# -*- coding: utf-8 -*-
import importlib
import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')
# import logging
# import tornado.log
# logger = logging.getLogger()
# tornado.log.enable_pretty_logging()
# logger.setLevel(logging.NOTSET)
# logger.info(123)
from pymongo import Connection
conn = Connection()
proxy = conn.proxy.proxy


if __name__ == '__main__':
    site = sys.argv[1]
    name = 'sites.%s' % site
    conf1 = importlib.import_module(name)
    reload(sys.modules[name])
    conf1 = importlib.import_module(name)
    DB = conf1.DB
    for i in DB.find():
        print i['_id']
