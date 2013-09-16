# -*- coding: utf-8 -*-

XPATH = {
    'title': "//div[@class='shop-name']/h1[@class='shop-title']/text()",
    'score': "//div[@class='comment-rst']/span/meta/@content",
    'location':
    "//div[@class='shop-location']/ul/li/span[contains(@itemprop, 'street-address')]/text()",
    # 'tel:'//div[@class='shop-location']/ul/li/span[contains(@itemprop,'tel')]/text()",
    'tel':
    "/html/body[@id='top']/div[@class='shop-wrap']/div[@class='main']/div[@class='shop-info shakeable']/div[@class='shop-info-con']/div[@class='pic-txt']/div[@class='txt']/div[@class='shop-location'][1]/ul/li[2]/span[@class='call']/text()",
    'intro':
    u"/html/body[@id='top']/div[@class='shop-wrap']/div[@class='main']/div[@class='shop-info shakeable']/div[@class='shop-info-con']/div[@class='pic-txt']/div[@class='txt']/div[@class='desc-info']/div/ul/li[em='餐厅简介：']/text()",
    'feture':
    "/html/body[@id='top']/div[@class='shop-wrap']/div[@class='main']/div[@class='shop-info shakeable']/div[@class='shop-info-con']/div[@class='pic-txt']/div[@class='txt']/div[@class='shop-location'][2]/ul/li/a[@class='feature J_feature-btn']/text()",
    'othertitle':
    u"/html/body[@id='top']/div[@class='shop-wrap']/div[@class='main']/div[@class='shop-info shakeable']/div[@class='shop-info-con']/div[@class='pic-txt']/div[@class='txt']/div[@class='desc-info']/div/ul/li[em='餐厅别名：']/text()",
    'opentime':
    "/html/body[@id='top']/div[@class='shop-wrap']/div[@class='main']/div[@class='shop-info shakeable']/div[@class='shop-info-con']/div[@class='pic-txt']/div[@class='txt']/div[@class='desc-info']/div/ul/li[3]/span[@class='J_full-cont']/text()",
    'price':
    "/html/body[@id='top']/div[@class='shop-wrap']/div[@class='main']/div[@class='shop-info shakeable']/div[@class='shop-info-con']/div[@class='shop-tit']/div[@class='comment-rst']/div[@class='rst-taste']/span[1]/strong[@class='stress']/text()",
    'taste':
    "/html/body[@id='top']/div[@class='shop-wrap']/div[@class='main']/div[@class='shop-info shakeable']/div[@class='shop-info-con']/div[@class='shop-tit']/div[@class='comment-rst']/div[@class='rst-taste']/span[@class='rst'][1]/strong/text()",
    'environment':
    "/html/body[@id='top']/div[@class='shop-wrap']/div[@class='main']/div[@class='shop-info shakeable']/div[@class='shop-info-con']/div[@class='shop-tit']/div[@class='comment-rst']/div[@class='rst-taste']/span[@class='rst'][2]/strong/text()",
    'service':
    "/html/body[@id='top']/div[@class='shop-wrap']/div[@class='main']/div[@class='shop-info shakeable']/div[@class='shop-info-con']/div[@class='shop-tit']/div[@class='comment-rst']/div[@class='rst-taste']/span[@class='rst'][3]/strong/text()",
    'bread': "/html/body[@id='top']/div[@class='breadcrumb']/b",
    'exist':
    "/html/body[@id='top']/div[@class='shop-wrap']/div[@class='main']/div[@class='shop-info shakeable']/div[@class='shop-info-con']/div[@class='suspend-receipts']/strong/text()",
}

MUST_LIST = ['title']

NAME = 'dianping'
START_URL = 'http://www.dianping.com/shop/'

import os
from zhw_crawler.settings import ROOT_DIR
from zhw_crawler.utils import get_id_range
ID_RANGE_PATH = os.path.join(ROOT_DIR, 'conf', 'ids_list_%s' % NAME)
ID_RANGE = get_id_range(ID_RANGE_PATH)
RESULT_PATH = os.path.join(ROOT_DIR, 'log', NAME)
