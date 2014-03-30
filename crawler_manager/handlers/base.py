# -*- coding:utf-8 -*-

from tornado.web import RequestHandler


class BaseHandler(RequestHandler):

    def write_error(self, status_code, **kwargs):
        self.render('error.html', status_code=status_code)
