#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
import importlib
import sys
# from conf import NAME, RANGE, DOC_TYPE
import lxml.html.soupparser as soupparser
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


def get_doc(page_id, doc_type):
    page_path = 'html/%s/%s.%s' % (NAME, page_id, doc_type)
    if os.path.isfile(page_path):
        with open(page_path) as f:
            # print page_path
            # if f.read() == '':
            #     print 'empty', page_path
            #     os.remove(page_path)
            #     return
            return f.read()


def parse_doc(page_id, doc_type):
    doc_data = get_doc(page_id, doc_type)
    if doc_data:
        if doc_type == 'html':
            dom = None
            # print page_id
            try:
                dom = soupparser.fromstring(doc_data)
            except:
                # print page_id
                try:
                    mpa = dict.fromkeys(range(32))
                    doc_data = doc_data.decode('utf-8')
                    doc_data = doc_data.translate(mpa)
                    dom = soupparser.fromstring(doc_data)
                except:
                    doc_data = doc_data.replace('\xb0', '')
                    dom = soupparser.fromstring(doc_data)
            # dom = lxml.html.fromstring(doc_data)
            # if dom:
            #     print 1
            return dom
        elif doc_type == 'json':
            return doc_data


def analyse_data():
    if len(RANGE) == 3:
        ids = [i for i in xrange(RANGE[0], RANGE[1], RANGE[2])]
    else:
        ids = RANGE
    for i in ids:
        # if not DB.find_one({'_id': int(i)}):
        dom = parse_doc(i, DOC_TYPE)
        if dom is not None:
            handler_dom(dom, i, NAME)


if __name__ == '__main__':
    site = sys.argv[1]
    while True:
        name = 'sites.%s' % site
        conf1 = importlib.import_module(name)
        reload(sys.modules[name])
        conf1 = importlib.import_module(name)
        NAME = conf1.NAME
        RANGE = conf1.RANGE
        DOC_TYPE = conf1.DOC_TYPE
        # print NAME, RANGE, DOC_TYPE
        handler_dom = conf1.handler_dom
        adir = 'html/%s' % NAME
        DB = conf1.DB
        _id = conf1._id
        analyse_data()
        DB.update({'_id': _id}, {'$set': {'read': 5}})
