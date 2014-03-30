from zhw_crawler.spiders.common import CommonSpider
from zhw_crawler.conf.dianping_conf import NAME, START_URL, RESULT_PATH, ID_RANGE


class DianpingSpider(CommonSpider):
    name = NAME
    start_url = START_URL
    result_path = RESULT_PATH
    id_range = ID_RANGE

    def __init__(self, name=None, **kwargs):
        CommonSpider.__init__(self, kwargs=kwargs)
