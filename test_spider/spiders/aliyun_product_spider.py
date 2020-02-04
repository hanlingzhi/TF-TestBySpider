import scrapy
import json
from scrapy.http import Request

from test_spider.util.constant import CONST
from test_spider.orm import spider_db
from test_spider.items import ProductItem
from test_spider.util.print_format_util import PrintFormatUtil

__author__ = 'hanlingzhi'

'''
create_date: 
    2019.7.30
usage: 
    阿里云产品爬虫
'''

class ALIProductSpider(scrapy.Spider):

    name = CONST.ALI_YUN_PRODUCT_SPIDER_NAME # 定义爬虫名

    allowed_domains = [CONST.ALI_YUN_DOMAIN]  # 接受处理的域名

    product_list = spider_db.get_product_all()

    def start_requests(self):
        PrintFormatUtil.print_line("阿里云已有的服务一共{}个".format(len(self.product_list)))
        yield Request(CONST.ALI_YUN_PRODUCT_URL, callback=self.parse, headers=CONST.ALI_YUN_HEADER)

    def parse(self, response):
        data = json.loads(response.body.decode('utf-8'))
        assert 'product' in data and len(data['product']) > 0, "URL{} 数据不符合要求 ".format(response.url)
        for category_1 in data['product']:
            if 'name' in data['product'][category_1]:
                PrintFormatUtil.print_line("处理一级类目{}".format(category_1))
                for service in data['product'][category_1]['name']:
                    item = ProductItem()
                    item['category1'] = service['category1']
                    if 'category2' in service:
                        item['category2'] = service['category2']
                    else:
                        item['category2'] = ''
                    item['title'] = service['title']
                    item['description'] = service['description']
                    item['link'] = service['textLink']
                    if "%s:%s" % (service['category1'], service['title']) not in self.product_list:
                        PrintFormatUtil.print_line("新增获取子服务{}".format(item))
                        yield item
