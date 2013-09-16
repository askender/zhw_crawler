# -*- coding: utf-8 -*-

NAME = 'doubanmovie'

START_URL = 'http://movie.douban.com/top250?start='

MUST_LIST = [u'title']

XPATH = {
    "score": u"div[@class='item']/div[@class='info']/div[@class='bd']/div[@class='star']/span",
    "list": u"/html[@class='ua-linux ua-webkit']/body/div[@id='wrapper']/div[@id='content']/div[@class='grid-16-8 clearfix']/div[@class='article']/ol[@class='grid_view']/li",
    "title": u"div[@class='item']/div[@class='info']/div[@class='hd']/a/span[@class='title'][1]",
}

import os
from zhw_crawler.settings import ROOT_DIR
from zhw_crawler.utils import get_id_range
ID_RANGE_PATH = os.path.join(ROOT_DIR, 'conf', 'ids_list_%s' % NAME)
ID_RANGE = get_id_range(ID_RANGE_PATH)
RESULT_PATH = os.path.join(ROOT_DIR, 'log', NAME)
