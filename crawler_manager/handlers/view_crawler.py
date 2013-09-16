# -*- coding:utf-8 -*-

from .base import BaseHandler


import urllib
import json
from urlparse import urljoin
from scrapy.utils.jsonrpc import jsonrpc_client_call
import requests


def cmd_list_resources(args, opts):
    """list-resources - list available web service resources"""
    return json_get(opts, '')['resources']


def cmd_list_available(args, opts):
    """list-available - list name of available spiders"""
    return jsonrpc_call(opts, 'crawler/spiders', 'list')


def cmd_list_running(args, opts):
    """list-running - list running spiders"""
    return json_get(opts, 'crawler/engine/open_spiders')


def cmd_start(args, opts):
    return jsonrpc_call(opts, 'crawler/engine', 'start')


def cmd_pause(args, opts):
    return jsonrpc_call(opts, 'crawler/engine', 'pause')


def cmd_stopall(args, opts):
    return jsonrpc_call(opts, 'crawler/engine', 'stop')


def cmd_open(args, opts):
    """stop <spider> - stop a running spider"""
    return jsonrpc_call(opts, 'crawler/engine', 'open_spider', args[0])


def cmd_stop(args, opts):
    """stop <spider> - stop a running spider"""
    jsonrpc_call(opts, 'crawler/engine', 'close_spider', args[0])


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


class ViewCrawlerHandler(BaseHandler):

    def get(self):
        listprojects_url = 'http://localhost:6800/listprojects.json'
        projects_status = projects = ''
        try:
            r = requests.get(listprojects_url, timeout=3)
        except requests.exceptions.RequestException as e:
            print(e)
        else:
            if r.status_code == requests.codes.ok:
                projects = r.text
        if projects:
            projects = json.loads(projects)
            projects_status = projects['status']
            projects = projects['projects']
        self.render(
            'view_crawler.html',
            projects_status=projects_status,
            projects=projects,
        )
