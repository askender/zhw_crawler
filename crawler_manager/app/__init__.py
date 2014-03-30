# -*- coding: utf-8 -*-
from logger import logger


class APP(object):

    def start(self):
        from task import Task
        Task().start()
        logger.info('APP started')
