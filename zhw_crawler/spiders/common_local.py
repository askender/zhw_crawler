#  -*- coding: utf-8-*-
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
import os
import re
from zhw_crawler.utils import filter_tags
from zhw_crawler.conf.common_conf import XPATH, RESULT_PATH
from zhw_crawler.items.common_item import Commonshop


class CommonLocalSpider(BaseSpider):
    name = ''
    xpath = XPATH
    result_path = RESULT_PATH

    def __init__(self, name=None, **kwargs):
        if not hasattr(self, 'start_urls'):
            self.start_urls = []
            file_list = [i for i in os.listdir(
                self.result_path) if i.endswith('.html')]
            for i in file_list:
                path = os.path.join(self.result_path, i).replace('?', '%3F')
                url = 'file://%s' % (path)
                self.start_urls.append(url)
        BaseSpider.__init__(self, kwargs=kwargs)
        self.item = Commonshop()

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        item = self.item
        url_no = response.url.split('/')[-1].replace('.html', '')
        if '-d' in url_no:
            url_no = re.findall(r"-d(.+?)-", url_no)[0]
        url_no = ''.join(i for i in url_no if i.isdigit())
        item['shopid'] = int(url_no)  # temp only int

        if 'list' in self.xpath:
            for sel in hxs.select(self.xpath['list']):
                for k, v in self.xpath.items():
                    if k != 'list':
                        value = sel.select(v).extract()
                        value = ''.join(value)
                        value = filter_tags(value)
                        item[k] = ' '.join(value.split())
                yield item
        else:
            for k, v in self.xpath.items():
                value = hxs.select(v).extract()
                value = ''.join(value)
                value = filter_tags(value)
                item[k] = ' '.join(value.split())
            yield item
