# -*- coding: utf-8 -*-

NAME = 'solidot/solidot_'
DOC_TYPE = 'html'
START_URL = 'http://www.solidot.org/story?sid='

# MUST_LIST = [u'title']

XPATH = {
    # "words": u".//div[@id='footer']/p[@class='famous']/text()",
    "title": u".//div[@class='ct_tittle']/div[@class='bg_htit']/h2/text()",
    "about": u".//div[@class='about_at']/div[@class='block_m']/div[@class='talk_time']/b/text()",
    "author": u".//div[@class='about_at']/div[@class='block_m']/div[@class='talk_time']/a[1]/text()",
    "time": u".//div[@class='about_at']/div[@class='block_m']/div[@class='talk_time']/text()",
    "topic": u".//div[@class='about_at']/div[@class='block_m']/div[@class='talk_time']/div[@class='icon_float']/a/@title",
    "hitnum": u".//div[@id='right']/div[@class='block_r']/div[@class='contentbox']/div[@class='content']/b/text()",
    "content": u".//div[@class='about_at']/div[@class='block_m']/div[@class='p_mainnew']",
}

RANGE = [0, 37527, 1]

# words = dom.xpath(XPATH['words'])
# words = words[0] if words else ''
# r = dom.xpath(XPATH['list'])
# for i in r:
#     title = i.xpath(XPATH['title'])
#     score = i.xpath(XPATH['score'])
#     print(title, score)
