import os


def get_proxies():
    proxies = []
    proxy_list = 'zhw_crawler/conf/proxy_list'
    if os.path.isfile(proxy_list):
        with open(proxy_list, 'r') as fp:
            for eachline in fp:
                proxies.append(eachline.replace('\n', ''))
    return proxies

proxies = get_proxies()
