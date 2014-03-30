from scrapy.item import Item, Field


class Daodaoshop(Item):

    shopid = Field()
    title = Field()
    address = Field()
    bread = Field()
    rank = Field()
    score = Field()
    like = Field()
    dislike = Field()
    shoptype = Field()
    description = Field()
    activity = Field()
