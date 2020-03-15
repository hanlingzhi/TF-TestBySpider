from collections import Iterable
from test_spider.orm.spider_db_model import AliProductTable, TestRecordTable

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
            products.append("%s:%s" % (p.category1, p.title))
    del product_data_list
    return products


def get_product_url_all():
    urls = []
    product_data_list = AliProductTable.select()
    if isinstance(product_data_list, Iterable):
        for p in product_data_list:
            urls.append(AliProduct(p.id, p.title, p.link))
    del product_data_list
    return urls


# save product
def save_product_item_to_db(item):
    data = AliProductTable(category1=item['category1'], category2=item['category2'], title=item['title'],
                           link=item['link'], description=item['description'])
    return data.save()

# save record
def save_record_item_to_db(item):
    data = TestRecordTable(tid=item['tid'], pid=item['pid'], pic_new=item['pic_new'],pic_old=item['pic_old'],
                           pl_ssim=item['pl_ssim'], cv_ssim=item['cv_ssim'], pic_pl_diff=item['pic_pl_diff'],
                           pic_oc_diff=item['pic_oc_diff']
                           )
    return data.save()

class AliProduct:

    def __init__(self, pid:int, name:str, url:str):
        self.pid = pid,
        self.p_name = name,
        self.p_url = url

    def get_id(self):
        if isinstance(self.pid, tuple):
            return self.pid[0]
        return self.pid

    def get_name(self):
        if isinstance(self.p_name, tuple):
            return self.p_name[0]
        return self.p_name

    def get_url(self):
        if isinstance(self.p_url, tuple):
            return self.p_url[0]
        return self.p_url
