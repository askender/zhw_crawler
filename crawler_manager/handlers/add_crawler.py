# -*- coding:utf-8 -*-

from .base import BaseHandler
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


conf_common = '''
import os
from zhw_crawler.settings import ROOT_DIR
from zhw_crawler.utils import get_id_range
ID_RANGE_PATH = os.path.join(ROOT_DIR, 'conf', 'ids_list_%s' % NAME)
ID_RANGE = get_id_range(ID_RANGE_PATH)
RESULT_PATH = os.path.join(ROOT_DIR, 'log', NAME)
'''
spider_common = '''
    name = NAME
    start_url = START_URL
    result_path = RESULT_PATH
    id_range = ID_RANGE

    def __init__(self, name=None, **kwargs):
        CommonSpider.__init__(self, kwargs=kwargs)
'''
spider_local_common = '''
    xpath = XPATH
    result_path = RESULT_PATH

    def __init__(self, name=None, **kwargs):
        CommonLocalSpider.__init__(self, kwargs=kwargs)
'''


class AddCrawlerHandler(BaseHandler):

    def get(self):
        self.render('add_crawler.html')

    def post(self):
        NAME = self.get_argument("NAME")
        START_URL = self.get_argument("START_URL")
        XPATH = self.get_argument("XPATH")
        MUST_LIST = self.get_argument("MUST_LIST", '')
        ID_LIST = self.get_argument("ID_LIST", '')
        spider_xpath = {}
        for i in XPATH.split('\r\n'):
            k = i.split(':')[0]
            v = u''.join(i.split(':')[1:])
            spider_xpath[k] = v
        spider_xpath_str = ''
        for k, v in spider_xpath.items():
            spider_xpath_str = u"%s    \"%s\": u\"%s\",\n" % (
                spider_xpath_str, k, v)
        spider_xpath_str = '{\n%s}' % spider_xpath_str

        backup_file = '%s_backup.txt' % NAME
        with open(backup_file, 'wb') as afile:
            afile.write('%s\n%s\n%s\n%s\n%s\n' % (NAME, START_URL, XPATH, MUST_LIST, ID_LIST)
                        )

        MUST_LIST = MUST_LIST.split(' ')

        conf_file = '%s_conf.py' % NAME
        with open(conf_file, 'wb') as afile:
            afile.write('# -*- coding: utf-8 -*-\n\n')
        with open(conf_file, 'ab') as afile:
            afile.write(
                ''.join([
                    "NAME = '%s'\n\n" % NAME,
                    "START_URL = '%s'\n\n" % START_URL,
                    "MUST_LIST = %s\n\n" % MUST_LIST,
                    "XPATH = %s\n" % spider_xpath_str,
                    "%s" % conf_common,
                ])
            )

        spider_item_str = ''
        for k in spider_xpath.keys():
            if k != 'list':
                spider_item_str = u"%s    %s = Field()\n" % (
                    spider_item_str, k)

        item_file = '%s_item.py' % NAME
        with open(item_file, 'wb') as afile:
            afile.write('# -*- coding: utf-8 -*-\n\n')
        with open(item_file, 'ab') as afile:
            afile.write(
                ''.join([
                    "from scrapy.item import Item, Field\n\n\n",
                    "class %s(Item):\n\n" % NAME.capitalize(),
                    "    shopid = Field()\n",
                    "%s" % spider_item_str,
                ])
            )

        spider_file = '%s.py' % NAME
        with open(spider_file, 'wb') as afile:
            afile.write('# -*- coding: utf-8 -*-\n\n')
        with open(spider_file, 'ab') as afile:
            afile.write(
                ''.join([
                    "from zhw_crawler.spiders.common import CommonSpider\n",
                    "from zhw_crawler.conf.%s_conf import NAME, START_URL, RESULT_PATH, ID_RANGE\n\n\n" % NAME,
                    "class %sSpider(CommonSpider):\n" % NAME.capitalize(),
                    "%s" % spider_common,
                ])
            )

        spider_local_file = '%s_local.py' % NAME
        with open(spider_local_file, 'wb') as afile:
            afile.write('# -*- coding: utf-8 -*-\n\n')
        with open(spider_local_file, 'ab') as afile:
            afile.write(
                ''.join([
                    "from zhw_crawler.spiders.common_local import CommonLocalSpider\n",
                    "from zhw_crawler.conf.%s_conf import XPATH, RESULT_PATH\n" % NAME,
                    "from zhw_crawler.items.%s_item import %s\n\n\n" % (
                        NAME, NAME.capitalize(),),
                    "class %sLocalSpider(CommonLocalSpider):\n" % NAME.capitalize(
                    ),
                    "    name = '%s_local'" % NAME,
                    "%s" % spider_local_common,
                    "        self.item = %s()\n" % NAME.capitalize(),
                ])
            )

        ids_list_file = 'ids_list_%s' % NAME
        with open(ids_list_file, 'wb') as afile:
            afile.write(ID_LIST)

        import os
        item_file_new = '../zhw_crawler/items/%s_item.py' % NAME
        conf_file_new = '../zhw_crawler/conf/%s_conf.py' % NAME
        spider_file_new = '../zhw_crawler/spiders/%s.py' % NAME
        spider_local_file_new = '../zhw_crawler/spiders/%s_local.py' % NAME
        ids_list_file_new = '../zhw_crawler/conf/ids_list_%s' % NAME
        os.rename(item_file, item_file_new)
        os.rename(conf_file, conf_file_new)
        os.rename(spider_file, spider_file_new)
        os.rename(spider_local_file, spider_local_file_new)
        os.rename(ids_list_file, ids_list_file_new)
