#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
from conf import NAME, DOC_TYPE, RANGE, XPATH
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import logging
import tornado.log
from logging.handlers import RotatingFileHandler
logger = logging.getLogger()
tornado.log.enable_pretty_logging()
logger.setLevel(logging.NOTSET)


def get_doc(page_id, doc_type):
    page_path = 'html/%s%s.%s' % (NAME, page_id, doc_type)
    if os.path.isfile(page_path):
        with open(page_path) as f:
            return f.read()


def parse_doc(page_id, doc_type):
    doc_data = get_doc(page_id, doc_type)
    if doc_data:
        if doc_type == 'html':
            # parser = lxml.etree.XMLParser(
            #     encoding='utf-8' #Your encoding issue.
            #     recover=True, # recover from bad xml
            # )
            # import lxml.html.soupparser as Soupparser
            # dom = Soupparser.fromstring(doc_data)
            import lxml.html
            dom = lxml.html.fromstring(doc_data)
            # words = dom.xpath(XPATH['words'])
            # words = words[0] if words else ''
            title = dom.xpath(XPATH['title'])
            title = title[0] if title else ''
            logger.info(page_id)
            logger.info(title)
            if title:
                print(title)
            # print(words)
            # r = dom.xpath(XPATH['list'])
            # for i in r:
            #     title = i.xpath(XPATH['title'])
            #     score = i.xpath(XPATH['score'])
            #     print(title, score)
        if doc_type == 'json':
            import json
            doc_json = json.loads(doc_data)
            # for i in doc_json['responseData']['results']:
            #     print(i['titleNoFormatting'])
            #     print(i['unescapedUrl'])
            #     print(i['content'])


def analyse_data():
    ids = [i for i in xrange(RANGE[0], RANGE[1], RANGE[2])]
    for i in ids:
        parse_doc(i, DOC_TYPE)


if __name__ == '__main__':
    analyse_data()
