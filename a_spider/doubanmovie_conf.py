# -*- coding: utf-8 -*-

NAME = 'doubanmovie250'
DOC_TYPE = 'html'
START_URL = 'http://movie.douban.com/top250?start='

# MUST_LIST = [u'title']

XPATH = {
    "score": u".//div[@class='star']/span/text()",
    "list": u".//div[@class='article']/ol/li",
    "title": u".//span[@class='title'][1]/text()",
}
