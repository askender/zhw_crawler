#!/usr/bin/python
#-*-coding:utf-8-*-
from scrapy import log
from scrapy.contrib.downloadermiddleware.retry import RetryMiddleware
from zhw_crawler.utils import import_class
from zhw_crawler.settings import CONFIG_PATH


class RetryLogMiddleware(RetryMiddleware):

    def _retry(self, request, reason, spider):
        spider_name = spider.name.replace('_local', '')
        import_str = '%s.%s_conf.RESULT_PATH' % (CONFIG_PATH, spider_name)
        result_path = import_class(import_str)
        retries = request.meta.get('retry_times', 0) + 1
        if retries <= self.max_retry_times:
            log.msg(
                format="Retrying %(request)s (failed %(retries)d times): %(reason)s",
                level=log.DEBUG, spider=spider, request=request, retries=retries, reason=reason)
            retryreq = request.copy()
            retryreq.meta['retry_times'] = retries
            retryreq.dont_filter = True
            retryreq.priority = request.priority + self.priority_adjust
            return retryreq
        else:
            log.msg(
                format="Gave up retrying %(request)s (failed %(retries)d times): %(reason)s",
                level=log.DEBUG, spider=spider, request=request, retries=retries, reason=reason)
            url_no = request.url.split('/')[-1]
            logfile = '%s/timeout.txt' % (result_path)
            with open(logfile, 'a') as afile:
                afile.write('%s\n' % url_no)
