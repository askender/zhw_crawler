# -*- coding: utf-8 -*-

NAME = 'dianping10000_'
DOC_TYPE = 'json'
START_URL = 'http://ajax.googleapis.com/\
ajax/services/search/web?v=2.0&q=site:www.dianping.com/shop&rsz=8&start='

# MUST_LIST = [u'title']

XPATH = {
    "score": u".//div[@class='star']/span/text()",
    "list": u".//div[@class='article']/ol/li",
    "title": u".//span[@class='title'][1]/text()",
}

RANGE = [0, 64, 8]
