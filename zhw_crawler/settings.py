#  -*- coding: utf-8-*-

SPIDER_MODULES = ['zhw_crawler.spiders']
NEWSPIDER_MODULE = 'zhw_crawler.spiders'
DEFAULT_ITEM_CLASS = 'zhw_crawler.items.common_item.Commonshop'


# scrapy's item pipelines have orders.
ITEM_PIPELINES = [
    'zhw_crawler.pipelines.filter.FilterPipeline',
    'zhw_crawler.pipelines.mongodb.MongodbStorePipeline',
    # 'zhw_crawler.pipelines.mysql.MysqlStorePipeline',
]

# if use local site, DOWNLOAD_DELAY = 0 will make things wrong
DOWNLOAD_DELAY = 0.1


DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.retry.RetryMiddleware': 90,
    'zhw_crawler.middlewares.randomproxy.RandomProxy': 100,
    'zhw_crawler.middlewares.retrylog.RetryLogMiddleware': 101,
    # 'zhw_crawler.middlewares.useragent.RotateUserAgentMiddleware': 101,
    # 'zhw_crawler.middlewares.google_cache.GoogleCacheMiddleware': 102,
    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
}

COOKIES_ENABLED = True

MONGODB_SERVER = "localhost"
MONGODB_NAME = "shops"
MONGODB_PORT = 27017

# USER_AGENT = 'pkg_spider (+http://www.zhaohaowan.com)'
USER_AGENT = '''
Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.31 \
(KHTML,like Gecko) Chrome/26.0.1410.43 Safari/537.31
'''

# To make RotateUserAgentMiddleware enable.
USE_PROXY = True  # True False

# Retry many times since proxies often fail
RETRY_TIMES = 3
# Retry on most error codes since proxies fail for different reasons
# RETRY_HTTP_CODES = [500, 503, 504, 400, 403, 408]

# REDIRECT_ENABLED = False

DOWNLOAD_TIMEOUT = 90


import os
ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
CONFIG_PATH = 'zhw_crawler.conf'

LOG_ENABLED = True
LOG_ENCODING = 'utf-8'
LOG_LEVEL = 'DEBUG'  # ERROR DEBUG
LOG_STDOUT = True
LOG_FILE = 'zhw_crawler/log/spider.log'


# WEBSERVICE_PORT = [6080, 7030]
