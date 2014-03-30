# -*- coding:utf-8 -*-

from base import BaseHandler


class ErrHandler(BaseHandler):

    def get(self):
        self.render('error.html', status_code=404)
