# -*- coding: utf-8 -*-

from zhw_crawler.spiders.common_local import CommonLocalSpider
from zhw_crawler.conf.daodao_google_conf import XPATH, RESULT_PATH
from zhw_crawler.items.daodao_google_item import Daodao_google


class Daodao_googleLocalSpider(CommonLocalSpider):
    name = 'daodao_google_local'
    xpath = XPATH
    result_path = RESULT_PATH

    def __init__(self, name=None, **kwargs):
        CommonLocalSpider.__init__(self, kwargs=kwargs)
        self.item = Daodao_google()
