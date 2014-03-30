# -*- coding: utf-8 -*-

NAME = 'daodao_google'

START_URL = 'https://www.google.com.hk/search?q=site:www.daodao.com+attraction_review&start='

MUST_LIST = [u'title']

XPATH = {
    "link": u"div/div/div/div[1]/div/div/ul/li[1]/a/@href",
    "bread": u"div[@class='rc']/div[@class='s']/div/div[@class='f kv']/cite[@class='bc']",
    "list": u"//div[@id='center_col']/div[@id='res']/div[@id='search']/div[@id='ires']/ol[@id='rso']/li[@class='g']",
    "score": u"div[@class='rc']/div[@class='s']/div/div[@class='f slp']",
    "title": u"div[@class='rc']/h3[@class='r']/a",
}

import os
from zhw_crawler.settings import ROOT_DIR
from zhw_crawler.utils import get_id_range
ID_RANGE_PATH = os.path.join(ROOT_DIR, 'conf', 'ids_list_%s' % NAME)
ID_RANGE = get_id_range(ID_RANGE_PATH)
RESULT_PATH = os.path.join(ROOT_DIR, 'log', NAME)
