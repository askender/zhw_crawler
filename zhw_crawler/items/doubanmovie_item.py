# -*- coding: utf-8 -*-

from scrapy.item import Item, Field


class Doubanmovie(Item):

    shopid = Field()
    score = Field()
    title = Field()
