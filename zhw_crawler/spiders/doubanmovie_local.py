# -*- coding: utf-8 -*-

from zhw_crawler.spiders.common_local import CommonLocalSpider
from zhw_crawler.conf.doubanmovie_conf import XPATH, RESULT_PATH
from zhw_crawler.items.doubanmovie_item import Doubanmovie


class DoubanmovieLocalSpider(CommonLocalSpider):
    name = 'doubanmovie_local'
    xpath = XPATH
    result_path = RESULT_PATH

    def __init__(self, name=None, **kwargs):
        CommonLocalSpider.__init__(self, kwargs=kwargs)
        self.item = Doubanmovie()
