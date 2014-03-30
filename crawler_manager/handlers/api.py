# -*- coding:utf-8 -*-

from base import BaseHandler
import json
import urllib
from urlparse import urljoin
from scrapy.utils.jsonrpc import jsonrpc_client_call


def cmd_get_spider_stats(args, opts):
    """get-spider-stats <spider> - get stats of a running spider"""
    return jsonrpc_call(opts, 'stats', 'get_stats', args[0])


def cmd_get_global_stats(args, opts):
    """get-global-stats - get global stats"""
    return jsonrpc_call(opts, 'stats', 'get_stats')


def get_wsurl(opts, path):
    return urljoin("http://%s:%s/" % (opts.host, opts.port), path)


def jsonrpc_call(opts, path, method, *args, **kwargs):
    url = get_wsurl(opts, path)
    return jsonrpc_client_call(url, method, *args, **kwargs)


def json_get(opts, path):
    url = get_wsurl(opts, path)
    return json.loads(urllib.urlopen(url).read())


class opts(object):
    host = 'localhost'
    port = 6080


class GlobalStatsHandler(BaseHandler):

    def get(self):
        try:
            global_stats = cmd_get_global_stats([], opts)
        except:
            global_stats = {}
        self.write(global_stats)


class SpiderStatsHandler(BaseHandler):

    def get(self, name):
        try:
            spider_stats = cmd_get_spider_stats([name], opts)
        except:
            spider_stats = {}
        self.write(spider_stats)
