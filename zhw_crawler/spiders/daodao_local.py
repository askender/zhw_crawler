#  -*- coding: utf-8-*-
from zhw_crawler.spiders.common_local import CommonLocalSpider
from zhw_crawler.conf.daodao_conf import XPATH, RESULT_PATH
from zhw_crawler.items.daodao_item import Daodaoshop


class DaodaoLocalSpider(CommonLocalSpider):
    name = 'daodao_local'
    xpath = XPATH
    result_path = RESULT_PATH

    def __init__(self, name=None, **kwargs):
        CommonLocalSpider.__init__(self, kwargs=kwargs)
        self.item = Daodaoshop()
