import requests
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from pymongo import Connection
conn = Connection()
proxy = conn.proxy.proxy


TEST_URL = 'http://baidu.com'


def export():
    for i in proxy.find():
        # if i['httptype'] == 'HTTP':
        if i['httptype'] in ['HTTP', 'HTTPS']:
            print '%s://%s' % (i['httptype'].lower(), i['ipport'])


def check_proxy_list():
    proxies = []
    # if os.path.isfile('proxy_list_raw_xici'):
    if os.path.isfile('proxy_list_newest'):
        with open('proxy_list_newest') as fp:
            for eachline in fp:
                proxy = eachline.replace('\n', '')
                # proxy1 = proxy.split('  ')[0].split(' ')[2].split('\t')
                # proxy1 = proxy.split('\t')
                # proxy2 = proxy.split('  ')[1].split('\t')
                # ip = proxy1[1]
                # port = proxy1[2]
                # proxy = '%s:%s' % (ip, port)
                proxies.append(proxy)
    for i in proxies:
        # proxies = {
        #     'http': 'http://%s' % i
        # }
        if proxy.startswith('https'):
            proxies = {
                'https': i
            }
        else:
            proxies = {
                'http': i
            }
        try:
            r = requests.get(TEST_URL, proxies=proxies, timeout=5)
        except Exception, e:
            print(i, e, 'err')
        else:
            if r.status_code == requests.codes.ok:
                with open('proxy_list_newest2', 'a') as afile:
                    afile.write('%s\n' % i)


if __name__ == '__main__':
    # export()
    check_proxy_list()
