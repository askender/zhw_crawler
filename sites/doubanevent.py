# -*- coding: utf-8 -*-
import re
# beijing shanghai guangzhou shenzhen
# wuhan chengdu hangzhou nanjing
# xian chongqing zhengzhou tianjin
# changsha suzhou fuzhou
# 北京 (2702989人) 上海 (1639090人) 广州 (1168754人) 深圳 (749549人)
# 武汉 (739408人) 成都 (697818人) 杭州 (619628人) 南京 (547589人)
# 西安 (513585人) 重庆 (460491人) 郑州 (432645人) 天津 (429224人)
# 长沙 (426230人) 苏州 (335395人) 福州 (298937人)
CITY = 'beijing'
NAME = 'douban_party_%s' % CITY
DOC_TYPE = 'html'
START_URL = 'http://www.douban.com/location/%s/events/future-party?start=' % CITY

# MUST_LIST = [u'title']
XPATH = {
    "list": u".//div[@class='article']/div/ul/li",
    "title": u"./div[@class='info']/div[@class='title']/a/span/text()",
    "link": u".//div[@class='info']/div[@class='title']/a/@href",
    "image": u".//div[@class='pic']/a/img/@src",
    "tags": u".//div[@class='info']/p/a/text()",
    "time": u".//div[@class='info']/ul[@class='event-meta']/li[@class='event-time']/text()",
    "place": u".//div[@class='info']/ul[@class='event-meta']/li[2]/text()",
    "starttime": u".//div[@class='info']/ul[@class='event-meta']/li[@class='event-time']/time[@itemprop='startDate']/@datetime",
    "endtime": u".//div[@class='info']/ul[@class='event-meta']/li[@class='event-time']/time[@itemprop='endDate']/@datetime",
    "fee": u".//div[@class='info']/ul[@class='event-meta']/li[@class='fee']/strong/text()",
    "owner": u".//div[@class='info']/ul[@class='event-meta']/li[4]/a/text()",
    "ownersite": u".//div[@class='info']/ul[@class='event-meta']/li[4]/a/@href",
    "join_count": u".//div[@class='info']/p[@class='counts']/span[1]/text()",
    "like_count": u".//div[@class='info']/p[@class='counts']/span[3]/text()",
    "total": u".//div[@class='article']/div/div[@class='paginator']/a[last()]/text()",
}

RANGE = [0, 70, 10]


def handler_dom(dom):
    r = dom.xpath(XPATH['list'])
    for i in r:
        tags = i.xpath(XPATH['tags'])
        time = i.xpath(XPATH['time'])
        place = i.xpath(XPATH['place'])
        title = i.xpath(XPATH['title'])[0]
        link = i.xpath(XPATH['link'])[0]
        image = i.xpath(XPATH['image'])[0]
        starttime = i.xpath(XPATH['starttime'])[0]
        endtime = i.xpath(XPATH['endtime'])[0]
        fee = i.xpath(XPATH['fee'])[0]
        owner = i.xpath(XPATH['owner'])[0]
        ownersite = i.xpath(XPATH['ownersite'])[0]
        join_count = i.xpath(XPATH['join_count'])[0]
        like_count = i.xpath(XPATH['like_count'])[0]
        time = ''.join(time).replace('\n', '').replace(' ', '')
        place = ''.join(place).replace('\n', '').replace(' ', '')
        tags = '&'.join(tags)
        _id = link.split('/')[-2]
        doc = {}
        doc['title'] = title
        doc['link'] = link
        doc['_id'] = _id
        doc['image'] = image
        doc['tags'] = tags
        doc['time'] = time
        doc['place'] = place
        doc['starttime'] = starttime
        doc['endtime'] = endtime
        doc['fee'] = fee
        doc['owner'] = owner
        doc['ownersite'] = ownersite
        doc['join_count'] = re.findall(r'[\d.]+', join_count)[0]
        doc['like_count'] = re.findall(r'[\d.]+', like_count)[0]
        yield doc
