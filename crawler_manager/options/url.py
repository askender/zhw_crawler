# -*- coding: utf-8 -*-

from handlers.index import IndexHandler
from handlers.add_crawler import AddCrawlerHandler
from handlers.view_crawler import ViewCrawlerHandler
from handlers.project import ProjectHandler
from handlers.other import ErrHandler
from handlers.api import GlobalStatsHandler
from handlers.api import SpiderStatsHandler

handlers = [
    (r"/", IndexHandler),
    (r"/add_crawler", AddCrawlerHandler),
    (r"/view_crawler", ViewCrawlerHandler),
    (r"/project", ProjectHandler),
    (r"/api/global_stats", GlobalStatsHandler),
    (r"/api/spider_stats/([^/]+)", SpiderStatsHandler),

    # Static Files
    # (r'/static/(.*)', StaticFileHandler, {
    #     'path': os.path.join(os.path.dirname(__file__), 'static'),
    # }),

    (r'/(.*)', ErrHandler),
    # Custom 404 ErrHandler, always put this at last

]
