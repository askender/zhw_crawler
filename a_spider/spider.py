#! /usr/bin/env python
# coding=utf-8

import os
import time
from requests.exceptions import Timeout
from common.requests_proxy import RequestsProxy
from conf import START_URL, XPATH, NAME, DOC_TYPE, RANGE


ses = RequestsProxy()


def _http_get(**kw):
    response = None
    try:
        response = ses.get(**kw)
    except Timeout as e:
        pass
        print(e)
    except Exception as e:
        pass
        print(e)
    if not response:
        pass
    return response


def _cache_doc(filename, htmldata):
    with open(filename, 'w') as f:
        f.write(htmldata)
        time.sleep(1)


def get_doc(page_id, doc_type):
    page_path = 'html/%s%s.%s' % (NAME, page_id, doc_type)
    if os.path.isfile(page_path):
        print(page_id, 'pass')
        return
        with open(page_path) as f:
            return f.read()
    r = _http_get(url='%s%s' % (START_URL, page_id), timeout=5)
    if r:
        _cache_doc(page_path, r.content)
        print(page_id, 'done')
        return r.content
    else:
        return None


def parse_doc(page_id, doc_type):
    doc_data = get_doc(page_id, doc_type)
    return
    if doc_data:
        if doc_type == 'html':
            import lxml.html.soupparser as Soupparser
            dom = Soupparser.fromstring(doc_data)
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


def get_data():
    ids = [i for i in xrange(RANGE[0], RANGE[1], RANGE[2])]
    print(ids)
    for i in ids:
        print(i)
        parse_doc(i, DOC_TYPE)


if __name__ == '__main__':
    get_data()
