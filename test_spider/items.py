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

# record item
class RecordItem(scrapy.Item):
    tid = scrapy.Field()
    pid = scrapy.Field()
    pic_new = scrapy.Field()
    pic_old = scrapy.Field()
    pl_ssim = scrapy.Field()
    cv_ssim = scrapy.Field()
    pic_pl_diff = scrapy.Field()
    pic_oc_diff = scrapy.Field()
    create_time = scrapy.Field()

    def __repr__(self):
        str_format = ''
        for keys in self.keys():
            str_format += "%s=[%s]|" % (keys, self.__getitem__(keys))
        return str_format
