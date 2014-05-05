#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
from tools.proxy import http_get
from conf import NAME, START_URL, RANGE, DOC_TYPE


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


def get_data():
    ids = [i for i in xrange(RANGE[0], RANGE[1], RANGE[2])]
    for i in ids:
        # print(i)
        get_doc(i, DOC_TYPE)


if __name__ == '__main__':
    get_data()
