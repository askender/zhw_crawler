# -*- coding: utf-8 -*-
from multiprocessing import Process
from tornado import ioloop
import requests
import time


class Task(Process):

    def run(self):
        self.io_loop = ioloop.IOLoop()
        self.io_loop.add_callback(self.start_checking_warn)
        self.io_loop.start()

    def start_checking_warn(self):
        self.check_warn()
        self.io_loop.add_callback(self.start_checking_warn)

    def check_warn(self):
        r = requests.get('http://localhost:6868/api/spider_stats/dianping')
        print(r.json())
        time.sleep(60)
