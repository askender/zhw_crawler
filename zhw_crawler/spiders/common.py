from scrapy.spider import BaseSpider
import os
from zhw_crawler.conf.common_conf import NAME, START_URL, RESULT_PATH, ID_RANGE


class CommonSpider(BaseSpider):
    name = NAME
    start_url = START_URL
    result_path = RESULT_PATH
    id_range = ID_RANGE
    # allowed_domains = ['']
    # handle_httpstatus_list = [
    #     301, 302, 400, 404, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509]

    def __init__(self, name=None, **kwargs):
        if not hasattr(self, 'start_urls'):
            self.start_urls = []
            skiplist = []
            skip_file = '%s/skip.txt' % self.result_path
            if not os.path.isdir(self.result_path):
                os.makedirs(self.result_path)
            if os.path.isfile(skip_file):
                with open(skip_file, 'r') as fp:
                    for eachline in fp:
                        shopid = eachline.replace('\n', '')
                        if shopid.isdigit():
                            skiplist.append(int(shopid))

            if len(self.id_range) == 2:
                for i in xrange(self.id_range[0], self.id_range[1]):
                    if i not in skiplist:
                        url = '%s%s' % (self.start_url, i)
                        self.start_urls.append(url)
            else:
                for i in self.id_range:
                    if i not in skiplist:
                        url = '%s%s' % (self.start_url, i)
                        self.start_urls.append(url)
        BaseSpider.__init__(self, kwargs=kwargs)

    def parse(self, response):
        url_no = response.url.split('/')[-1]
        filename = '%s/%s.html' % (self.result_path, url_no)
        if response.status == 200:
            with open(filename, 'wb') as afile:
                afile.write(response.body)
        else:
            logfile = '%s/%s.txt' % (self.result_path, response.status)
            with open(logfile, 'a') as afile:
                afile.write('%s\n' % url_no)
