# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobItem(scrapy.Item):
    id = scrapy.Field()  # "68734"
    title = scrapy.Field()  # Python developer
    tags = scrapy.Field()  # ["ptyhon", "django"]
