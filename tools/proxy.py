#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import os
from random import randint, choice
from struct import unpack
from urlparse import urlparse
import requests
from requests.exceptions import Timeout


class RequestsProxy():

    """
    print('Please select your network:\n\
          1. CERNET(The China Education and Research Network)\n\
          2. CTCNET(China Telecommunications Corporation)\n\
          3. CNCNET(China NetCom)\n\
          4. DXT(Dian Xin Tong)\n')
    i = int(input('Input the number: '))
    if i==1:
        proxy_host = 'h' + str(random.randint(0,10)) + '.edu.bj.ie.sogou.com'
    elif i==2:
        proxy_host = 'h' + str(random.randint(0,3)) + '.ctc.bj.ie.sogou.com'
    elif i==3:
        proxy_host = 'h' + str(random.randint(0,3)) + '.cnc.bj.ie.sogou.com'
    elif i==4:
        proxy_host = 'h' + str(random.randint(0,10)) + '.dxt.bj.ie.sogou.com'
    """

    def __init__(self):
        pass

    x_sogou_auth = '9CD285F1E7ADB0BD403C22AD1D545F40/30/853edc6d49ba4e27'
    session = requests.session()

    @staticmethod
    def _get_proxy_host():
        proxy_host = 'http://h%s.edu.bj.ie.sogou.com' % str(randint(0, 10))
        # proxy_host = 'http://h%s.cnc.bj.ie.sogou.com' % str(randint(0, 3))
        # proxy_host = 'http://h%s.dxt.bj.ie.sogou.com' % str(randint(0, 10))
        # proxy_host = 'http://h%s.ctc.bj.ie.sogou.com' % str(randint(0, 3))
        return proxy_host

    def get(self, url, **kwargs):
        return self.request('get', url, **kwargs)

    def post(self, url, **kwargs):
        return self.request('post', url, **kwargs)

    def request(self, method, url, **kwargs):
        if 'headers' not in kwargs:
            kwargs['headers'] = {}
        if url[:7].lower() != 'http://':
            url = 'http://%s' % url

        host = urlparse(url).netloc
        kwargs['headers']["X-Sogou-Auth"] = self.x_sogou_auth
        t = hex(int(time.time()))[2:].rstrip('L').zfill(8)
        kwargs['headers']["X-Sogou-Tag"] = _calc_sogou_hash(t, host)
        kwargs['headers']["X-Sogou-Timestamp"] = t
        proxies = {
            'http': self._get_proxy_host()
        }
        kwargs['proxies'] = proxies
        return self.session.request(method, url, **kwargs)


def _calc_sogou_hash(t, host):
    s = (t + host + 'SogouExplorerProxy').encode('ascii')
    code = len(s)
    dwords = int(len(s) / 4)
    rest = len(s) % 4
    v = unpack(str(dwords) + 'i' + str(rest) + 's', s)
    for vv in v:
        if isinstance(vv, type('i')):
            break
        # noinspection PyTypeChecker
        vv = int(vv)
        a = (vv & 0xFFFF)
        b = (vv >> 16)
        code += a
        code ^= ((code << 5) ^ b) << 0xb
        # To avoid overflows
        code &= 0xffffffff
        code += code >> 0xb
    if rest == 3:
        code += ord(s[len(s) - 2]) * 256 + ord(s[len(s) - 3])
        code ^= (code ^ (ord(s[len(s) - 1]) * 4)) << 0x10
        code &= 0xffffffff
        code += code >> 0xb
    elif rest == 2:
        code += ord(s[len(s) - 1]) * 256 + ord(s[len(s) - 2])
        code ^= code << 0xb
        code &= 0xffffffff
        code += code >> 0x11
    elif rest == 1:
        code += ord(s[len(s) - 1])
        code ^= code << 0xa
        code &= 0xffffffff
        code += code >> 0x1
    code ^= code * 8
    code &= 0xffffffff
    code += code >> 5
    code ^= code << 4
    code &= 0xffffffff
    code += code >> 0x11
    code ^= code << 0x19
    code &= 0xffffffff
    code += code >> 6
    code &= 0xffffffff
    return hex(code)[2:].rstrip('L').zfill(8)

req = RequestsProxy()


def get_proxies():
    proxies = []
    proxy_list = 'tools/proxy_list'
    if os.path.isfile(proxy_list):
        with open(proxy_list) as fp:
            for eachline in fp:
                proxies.append(eachline.replace('\n', ''))
    return proxies


def http_get(url):
    proxies = get_proxies()
    proxies = {
        'http': 'http://%s' % choice(proxies)
    }
    response = None
    try:
        # response = req.get(**kw)
        response = requests.get(url=url, proxies=proxies, timeout=5)
    except Timeout as e:
        print 'timeout'
    except Exception as e:
        print(e)
    return response
    time.sleep(1)  # be gentle

if __name__ == '__main__':

    r = http_get(url='http://baidu.com')
    print(r.content)
    # url = 'http://m.dianping.com/shop/6162303'
    # print ses.get(url).content
