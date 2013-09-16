#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import tornado.httpserver
import tornado.ioloop
import tornado.web
from logger import logger
from options.url import handlers
import options
from app import APP


application = tornado.web.Application(handlers, **options.web_server)
http_server = tornado.httpserver.HTTPServer(application, xheaders=True)


def launch(port):
    APP().start()
    http_server.listen(port)
    logger.info('Server started on http://localhost:%s' % port)
    tornado.ioloop.IOLoop.instance().start()


parser = argparse.ArgumentParser(
    description='Welcome to Crawler Maker')
parser.add_argument(
    '-p', '--port',
    dest='port',
    action='store',
    type=int,
    default=options.port,
    help='run on the given port'
)


if __name__ == '__main__':
    args = parser.parse_args()
    port = args.port
    launch(port)
