#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 2718
import os
from tools.proxy import http_get
from conf import DOC_TYPE, handler_dom, XPATH
import lxml.html.soupparser as soupparser
from pymongo import Connection
conn = Connection()
party = conn.party.party
import read


def _cache_doc(filename, htmldata):
    with open(filename, 'w') as f:
        f.write(htmldata)


def get_doc(page_id, doc_type):
    page_path = 'html/%s%s.%s' % (NAME, page_id, doc_type)
    if os.path.isfile(page_path):
        # print(page_id, 'pass')
        return
    r = http_get(url='%s%s' % (START_URL, page_id))
    if r:
        _cache_doc(page_path, r.content)
        # print(page_id, 'done')
        return
    else:
        get_doc(page_id, doc_type)


def read_doc(page_id, doc_type):
    page_path = 'html/%s%s.%s' % (NAME, page_id, doc_type)
    if os.path.isfile(page_path):
        with open(page_path) as f:
            return f.read()


def check_doc(page_id, doc_type):
    doc_data = read_doc(page_id, doc_type)
    if doc_data:
        if doc_type == 'html':
            dom = soupparser.fromstring(doc_data)
            for r in handler_dom(dom):
                ret = party.find_one({'_id': r['_id']})
                if ret:
                    return 1
                else:
                    return 0


def check_total(page_id, doc_type):
    total = 0
    doc_data = read_doc(page_id, doc_type)
    if doc_data:
        if doc_type == 'html':
            dom = soupparser.fromstring(doc_data)
            total = dom.xpath(XPATH['total'])[0]
            return int(total)


def get_data():
    i = 0
    get_doc(0, DOC_TYPE)
    total = check_total(0, DOC_TYPE) * 10
    print 'total', total
    while i < total:
        get_doc(i, DOC_TYPE)
        if check_doc(i, DOC_TYPE):
            print 'found'
            break
            return
        else:
            print 'new'
            pass
        i += 10
    return total

if __name__ == '__main__':
    citys = ['beijing', 'shanghai', 'guangzhou', 'shenzhen', 'wuhan', 'chengdu', 'hangzhou',
             'nanjing', 'xian', 'chongqing', 'zhengzhou', 'tianjin', 'changsha', 'suzhou', 'fuzhou']
    citys = ['changsha']
    for i in citys:
        CITY = i
        NAME = 'douban_party_%s' % CITY
        START_URL = 'http://www.douban.com/location/%s/events/future-party?start=' % CITY
        total = get_data()
        ids = [i for i in xrange(0, total, 10)]
        print ids
        for i in ids:
            print i
            dom = read.parse_doc(i, DOC_TYPE)
            print dom, 111
            if dom is not None:
                for r in handler_dom(dom):
                    r['location'] = CITY
                    r['type'] = 'party'
                    print CITY, r['_id']
                    if not party.find_one({'_id': r['_id']}):
                        party.insert(r)
                        print 123
