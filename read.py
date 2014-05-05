#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
from conf import NAME, RANGE, DOC_TYPE
import lxml.html.soupparser as soupparser
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')
# import logging
# import tornado.log
# logger = logging.getLogger()
# tornado.log.enable_pretty_logging()
# logger.setLevel(logging.NOTSET)
# logger.info(123)


def get_doc(page_id, doc_type):
    page_path = 'html/%s%s.%s' % (NAME, page_id, doc_type)
    if os.path.isfile(page_path):
        with open(page_path) as f:
            return f.read()


def parse_doc(page_id, doc_type):
    doc_data = get_doc(page_id, doc_type)
    if doc_data:
        if doc_type == 'html':
            dom = soupparser.fromstring(doc_data)
            # dom = lxml.html.fromstring(doc_data)
            return dom
        if doc_type == 'json':
            return doc_data


def analyse_data():
    ids = [i for i in xrange(RANGE[0], RANGE[1], RANGE[2])]
    for i in ids:
        yield parse_doc(i, DOC_TYPE)

if __name__ == '__main__':
    analyse_data()
