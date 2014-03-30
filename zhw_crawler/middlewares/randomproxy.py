import random
from zhw_crawler.settings import USE_PROXY
from zhw_crawler.conf.update_proxies import update_proxies
from zhw_crawler.conf.proxies import proxies
from scrapy import log
import os
import sys


class RandomProxy(object):

    def __init__(self):
        self.proxies = proxies

    def process_request(self, request, spider):
        request.meta['handle_httpstatus_all'] = True
        if not request.url.startswith('http://localhost') and USE_PROXY and self.proxies:
            proxy = random.choice(self.proxies)
            request.meta['proxy'] = "http://%s" % proxy
            log.msg(
                'Using proxy <%s>, %d proxies left' % (
                    proxy, len(self.proxies)),
                level=log.DEBUG, spider=spider)

    def process_exception(self, request, exception, spider):
        if not request.url.startswith('http://localhost') and USE_PROXY and self.proxies:
            log.msg(
                'exception:%s' % exception,
                level=log.DEBUG, spider=spider)
            proxy = request.meta.get('proxy', '')
            if len(self.proxies) < len(proxies) / 4:
                pid = os.fork()
                if pid == 0:
                    update_proxies(flag=True)
                    sys.exit(0)
                if proxies:
                    self.proxies = proxies
            if len(self.proxies) < len(proxies) / 8:
                pid = os.fork()
                if pid == 0:
                    update_proxies()
                    sys.exit(0)
                if proxies:
                    self.proxies = proxies
            try:
                if len(self.proxies) > len(proxies) / 6:
                    self.proxies.remove(proxy.replace('http://', ''))
                else:
                    if proxies:
                        self.proxies = proxies
            except ValueError:
                log.msg(
                    'Remove failed',
                    level=log.DEBUG, spider=spider)
            log.msg(
                'Removing failed proxy <%s>, %d proxies left' % (
                    proxy, len(self.proxies)),
                level=log.DEBUG, spider=spider)
