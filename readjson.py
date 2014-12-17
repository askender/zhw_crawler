#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import re
import os


def get_list():
    ids = []
    with open('xx_bad') as f:
        for i in f:
            i = i.replace('\n', '')
            ids.append(i)
    return ids


def get_doc(i):
    path = 'html/airjson/%s.json' % i
    if not os.path.isfile(path):
        return []
    with open(path) as f:
        doc = f.read()
        doc = doc.replace('\n', '')
        comma_re = re.compile(',+')
        doc = comma_re.sub(',', doc)
        doc = doc.replace('[,', '[')
        doc = doc[4:]
        if doc.endswith('</html>'):
            print i
            os.remove(path)
            return []
        try:
            doc = json.loads(doc)
        except:
            return []
    return doc


def get_idx(idx_old, doc):
    for idx, i in enumerate(doc):
        idx_new = "%s[%s]" % (idx_old, idx)
        if isinstance(i, (list)):
            get_idx(idx_new, i)
        else:
            pass
            # print idx_new, i

for i in get_list():
    doc = get_doc(i)
    get_idx('', doc)



# https://www.google.com/search?tbm=map&hl=zh-CN&q=ABG%20airport
