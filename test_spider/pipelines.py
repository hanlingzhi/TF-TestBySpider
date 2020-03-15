# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from test_spider.util.print_format_util import PrintFormatUtil
from test_spider.orm import spider_db
from test_spider.util.counter import SpiderCounter
from test_spider.util.constant import CONST

class TestSpiderPipeline(object):

    counter = {}

    def open_spider(self, spider):
        PrintFormatUtil.print_title(" spider %s started " % spider.name)
        PrintFormatUtil.print_line(self.__class__.__name__)
        self.counter[spider.name] = SpiderCounter()
        self.counter[spider.name].create_counter()

    def close_spider(self, spider):
        PrintFormatUtil.print_line(self.__class__.__name__)
        total = self.counter[spider.name].total()
        PrintFormatUtil.print_line("total %s record inserted" % total)
        PrintFormatUtil.print_title(" spider %s finished " % spider.name)

    def process_item(self, item, spider):
        PrintFormatUtil.print_line(self.__module__)
        if spider.name == CONST.ALI_YUN_PRODUCT_SPIDER_NAME:
            result = spider_db.save_product_item_to_db(item)
        if spider.name == CONST.ALI_YUN_WEB_SPIDER_NAME:
            result = spider_db.save_record_item_to_db(item)
        if result == 1:
            PrintFormatUtil.print_success("spider %s success ..." % str(item).strip())
            self.counter[spider.name].add()
        else:
            PrintFormatUtil.print_error("spider %s fail ..." % str(item).strip())
        return item
