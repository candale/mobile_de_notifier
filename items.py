import scrapy


class CarItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    price = scrapy.Field()
    seller_info = scrapy.Field()
    photos_urls = scrapy.Field()
