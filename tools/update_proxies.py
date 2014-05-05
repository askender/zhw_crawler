import requests
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

TEST_URL = 'http://baidu.com'


def check_proxy_list():
    proxies = []
    if os.path.isfile('proxy_list_raw'):
        with open('proxy_list_raw') as fp:
            for eachline in fp:
                proxy = eachline.replace('\n', '')
                proxy1 = proxy.split('  ')[0].split(' ')[2].split('\t')
                # proxy2 = proxy.split('  ')[1].split('\t')
                ip = proxy1[1]
                port = proxy1[2]
                proxy = '%s:%s' % (ip, port)
                proxies.append(proxy)
    for i in proxies:
        proxies = {
            'http': 'http://%s' % i
        }
        try:
            r = requests.get(TEST_URL, proxies=proxies, timeout=5)
        except:
            print(i, 'err')
        else:
            if r.status_code == requests.codes.ok:
                with open('proxy_list', 'a') as afile:
                    afile.write('%s\n' % i)


if __name__ == '__main__':
    check_proxy_list()
