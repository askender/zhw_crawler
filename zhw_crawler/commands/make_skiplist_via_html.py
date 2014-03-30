#!/usr/bin/python
#-*-coding:utf-8-*-

import sys
import os


def make_skiplist_via_html(spider_name):
    result_path = 'zhw_crawler/log/%s/' % spider_name
    skip_ids = []
    file_list = [
        i for i in os.listdir(os.path.abspath(result_path)) if i.endswith('.html')]
    for i in file_list:
        skip_id = i.replace('.html', '')
        if spider_name == 'daodao':
            import re
            skip_id = re.findall(r"-d(.+?)-", skip_id)
        if skip_id:
            skip_id = skip_id[0]
        print(skip_id)
        skip_ids.append(skip_id)

if __name__ == "__main__":
    make_skiplist_via_html(sys.argv[1])
