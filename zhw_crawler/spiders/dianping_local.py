from zhw_crawler.spiders.common_local import CommonLocalSpider
from zhw_crawler.conf.dianping_conf import XPATH, RESULT_PATH
from zhw_crawler.items.dianping_item import Dianpingshop


class DianpingLocalSpider(CommonLocalSpider):
    name = 'dianping_local'
    xpath = XPATH
    result_path = RESULT_PATH

    def __init__(self, name=None, **kwargs):
        CommonLocalSpider.__init__(self, kwargs=kwargs)
        self.item = Dianpingshop()
