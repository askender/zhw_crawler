#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import importlib
from tools.proxy import http_get


def _cache_doc(filename, htmldata):
    with open(filename, 'w') as f:
        f.write(htmldata)


def get_doc(page_id, doc_type):
    page_path = 'html/%s/%s.%s' % (NAME, page_id, doc_type)
    if os.path.isfile(page_path):
        # print(page_id, 'pass')
        return
    url = make_url(START_URL, page_id)
    with open(page_path, 'w') as f:
        f.write('')
    r = http_get(url=url)
    if r:
        _cache_doc(page_path, r.content)
        # print(page_id, 'done')
        return
    else:
        try:
            os.remove(page_path)
        except:
            print 0


def get_data():
    dirpath = 'html/%s' % NAME
    if not os.path.isdir(dirpath):
        print dirpath
        os.mkdir(dirpath)
    if len(RANGE) == 3:
        ids = [i for i in xrange(RANGE[0], RANGE[1], RANGE[2])]
    else:
        ids = RANGE
    for i in ids:
        # print(i)
        get_doc(i, DOC_TYPE)


if __name__ == '__main__':
    site = sys.argv[1]
    # while True:
    name = 'sites.%s' % site
    conf1 = importlib.import_module(name)
    reload(sys.modules[name])
    conf1 = importlib.import_module(name)
    NAME = conf1.NAME
    START_URL = conf1.START_URL
    RANGE = conf1.RANGE
    DOC_TYPE = conf1.DOC_TYPE
    make_url = conf1.make_url
    print NAME, START_URL, len(RANGE), DOC_TYPE, make_url
    # adir = 'html/%s' % NAME
    # asum = sum([len(files) for root, dirs, files in os.walk(adir)])
    # if asum == conf1.TOTAL:
    #     _id = conf1._id
    #     db.update({'_id': _id}, {'$set': {'done': 1}})
    #     print 'done'
        # sys.exit(0)
    get_data()
