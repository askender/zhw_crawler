from scrapy.item import Item, Field


class Dianpingshop(Item):

    shopid = Field()
    title = Field()
    score = Field()
    location = Field()
    tel = Field()
    feture = Field()
    othertitle = Field()
    intro = Field()
    opentime = Field()
    price = Field()
    taste = Field()
    environment = Field()
    service = Field()
    bread = Field()
    exist = Field()
