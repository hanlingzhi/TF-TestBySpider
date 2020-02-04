# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

# product item
class ProductItem(scrapy.Item):
    category1 = scrapy.Field()
    category2 = scrapy.Field()
    title = scrapy.Field()
    create_time = scrapy.Field()
    description = scrapy.Field()
    link = scrapy.Field()

    def __str__(self):
        str_format = ''
        for keys in self.keys():
            str_format += "%s=[%s]|" % (keys, self.__getitem__(keys))
        return str_format
