import requests
import os

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

TEST_URL = 'http://bae.vipwp.me/tools/checkip.php'
PROXY_URL = 'http://bae.vipwp.me/tools/proxy.php?pwd=wp'

homedir = os.path.abspath(os.path.dirname(__file__))
proxy_list_raw = os.path.join(homedir, 'proxy_list_raw')
proxy_list = os.path.join(homedir, 'proxy_list')
proxy_list_new = os.path.join(homedir, 'proxy_list_new')
proxy_list_flag = os.path.join(homedir, 'proxy_list_flag')


def update_proxies(flag=None):
    if flag and os.path.isfile(proxy_list_flag):
        return
    open(proxy_list_flag, 'a').close()
    try:
        r = requests.get(PROXY_URL, timeout=60)
    except:
        print('err')
    else:
        if r.status_code == requests.codes.ok:
            with open(proxy_list_raw, 'wb') as afile:
                afile.write(r.text)
    check_proxy_list(flag)


def check_proxy_list(flag):
    proxies = []
    if os.path.isfile(proxy_list_raw):
        with open(proxy_list_raw, 'r') as fp:
            for eachline in fp:
                if not eachline.startswith('#'):
                    proxy = eachline.replace('\r', '').replace('\n', '')
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
                if 'http_xroxy_connection' in r.text:
                    with open(proxy_list_new, 'a') as afile:
                        afile.write('%s\n' % i)
    os.rename(proxy_list_new, proxy_list)
    if flag:
        os.remove(proxy_list_flag)


if __name__ == '__main__':
    update_proxies()
