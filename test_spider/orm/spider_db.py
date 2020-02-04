from collections import Iterable
from test_spider.orm.spider_db_model import AliProductTable

__author__ = 'hanlingzhi'

'''
create_date: 2019.4.4
usage: 数据库操作类
'''

# select product data
def get_product_all():
    products = []
    product_data_list = AliProductTable.select()
    if isinstance(product_data_list, Iterable):
        for p in product_data_list:
            products.append("%s:%s:%s" % (p.category1, p.category2, p.title))
    del product_data_list
    return products

# save product
def save_product_item_to_db(item):
    data = AliProductTable(category1=item['category1'], category2=item['category2'], title=item['title'], link=item['link'], description=item['description'])
    return data.save()

