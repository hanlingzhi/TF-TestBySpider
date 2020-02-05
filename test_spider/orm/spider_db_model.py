import datetime

from test_spider.util.constant import CONST
from peewee import *


__author__ = 'hanlingzhi'

'''
create_date: 2019.4.4
usage: data model
'''

# connect mysql
database = \
    MySQLDatabase(CONST.SPIDER_DB_INFO['database'],
                  **{'charset': 'utf8',
                     'passwd': CONST.SPIDER_DB_INFO['password'],
                     'user': CONST.SPIDER_DB_INFO['user'],
                     'host': CONST.SPIDER_DB_INFO['host'],
                     'port': CONST.SPIDER_DB_INFO['port'],
                     'use_unicode': True})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    id = BigAutoField()

    class Meta:
        database = database
        order_by = ('id',)

# ali_yun product table
class AliProductTable(BaseModel):
    category1 = CharField()
    category2 = CharField()
    create_time = DateTimeField(default=datetime.datetime.now)
    title = CharField()
    description = CharField()
    link = CharField()

    class Meta:
        table_name = 'ali_yun_product'

