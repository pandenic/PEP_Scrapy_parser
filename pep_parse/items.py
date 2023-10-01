"""Contains items description."""
import scrapy


class PepParseItem(scrapy.Item):
    """Describe fields of item in PepParse."""

    number = scrapy.Field()
    name = scrapy.Field()
    status = scrapy.Field()
