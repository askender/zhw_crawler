# -*- coding: utf-8 -*-

XPATH = {
    'title':
    "/html/body[@class='domn_zh_CN   ']/div[@id='PAGE']/div[@id='mainWrap']/div[@id='mainWrapInner']/div[@id='MAIN']/div[@id='HDPR_V1']/div[@class='col balance']/div[@id='HEADING_GROUP']/div/h1[@id='HEADING']/text()",
    'address': "//address/span/span[@class='format_address']",
    'bread':
    "/html/body[@class='domn_zh_CN   ']/div[@id='PAGE']/div[@id='mainWrap']/div[@id='mainWrapInner']/div[@id='MAIN']/div[@class='crumbs clearfix']/div[1]/ul/li/ul/li",
    'rank': "//div[@class='slim_ranking']/b[@class='rank_text']/text()",
    'score':
    "//span[contains(@class, 'rate rate_no')]/img[@class='sprite-ratings']/@content",
    'like':
    "/html/body[@class='domn_zh_CN   ']/div[@id='PAGE']/div[@id='mainWrap']/div[@id='mainWrapInner']/div[@id='MAIN']/div[@id='HDPR_V1']/div[@class='col balance']/div[@id='REVIEWS']/div[@class='summary-bd clearfix']/div[@class='summary-box clearfix']/div[@class='like clearfix']/ul[@class='clearfix']/li",
    'dislike':
    "/html/body[@class='domn_zh_CN   ']/div[@id='PAGE']/div[@id='mainWrap']/div[@id='mainWrapInner']/div[@id='MAIN']/div[@id='HDPR_V1']/div[@class='col balance']/div[@id='REVIEWS']/div[@class='summary-bd clearfix']/div[@class='summary-box clearfix']/div[@class='like clearfix']/ul[@class='clearfix']/li",
    'dislike':
    "/html/body[@class='domn_zh_CN   ']/div[@id='PAGE']/div[@id='mainWrap']/div[@id='mainWrapInner']/div[@id='MAIN']/div[@id='HDPR_V1']/div[@class='col balance']/div[@id='REVIEWS']/div[@class='summary-bd clearfix']/div[@class='summary-box clearfix']/div[@class='dislike clearfix']/ul[@class='clearfix']/li",
    'shoptype':
    u"/html/body[@class='domn_zh_CN   ']/div[@id='PAGE']/div[@id='mainWrap']/div[@id='mainWrapInner']/div[@id='MAIN']/div[@id='HDPR_V1']/div[@class='col balance']/div/div[@class='full_wrap clearfix']/div[@class='col2of2']/div[@class='listing_details']/div[@class='detail'][b='类型：']/text()",
    'activity':
    u"/html/body[@class='domn_zh_CN   ']/div[@id='PAGE']/div[@id='mainWrap']/div[@id='mainWrapInner']/div[@id='MAIN']/div[@id='HDPR_V1']/div[@class='col balance']/div/div[@class='full_wrap clearfix']/div[@class='col2of2']/div[@class='listing_details']/div[@class='detail'][b='活动：']/text()",
    'description':
    "/html/body[@class='domn_zh_CN   ']/div[@id='PAGE']/div[@id='mainWrap']/div[@id='mainWrapInner']/div[@id='MAIN']/div[@id='HDPR_V1']/div[@class='col balance']/div/div[@class='full_wrap clearfix']/div[@class='col2of2']/div[@class='listing_details']/div[@class='listing_description']",
}

MUST_LIST = ['title']
NAME = 'daodao'
START_URL = 'http://www.daodao.com/Attraction_Review-g298564-d'

# ID_RANGE = [0,100]
ID_RANGE = 'ids_list_%s' % NAME


import os
from zhw_crawler.settings import ROOT_DIR

ID_RANGE_PATH = os.path.join(ROOT_DIR, 'conf', ID_RANGE)
from zhw_crawler.utils import get_id_range
ID_RANGE = get_id_range(ID_RANGE_PATH)


RESULT_PATH = os.path.join(ROOT_DIR, 'log', NAME)
