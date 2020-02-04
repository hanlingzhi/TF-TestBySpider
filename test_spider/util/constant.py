__author__ = 'hanlingzhi'

'''
create_date: 2019.4.3
usage: Const
'''

class _Const:

  class ConstError(TypeError): pass

  class ConstCaseError(ConstError):
      def __init__(self):
          pass

  def __setattr__(self, name, value):
      if not name.isupper():
          raise self.ConstCaseError(' Const "%s" must be uppercase ' % name)
      if name in self.__dict__:
          raise self.ConstError("Cannot modify %s value" % name)
      self.__dict__[name] = value

CONST = _Const()

CONST.ALI_YUN_DOMAIN = 'aliyun.com'

CONST.ALI_YUN_PRODUCT_URL = 'https://query.aliyun.com/rest/topbar.view.product.all'

CONST.ALI_YUN_PRODUCT_SPIDER_NAME = 'ali_product_spider'

CONST.ALI_YUN_HEADER = {
    'Content-type': 'application/json; charset=utf-8',
}

CONST.SPIDER_DB_INFO = {
    'database': 'qa_plat',
    'host': '**********',
    'user': 'dev_qa_plat_writer',
    'password': 'VUDQWApJs3ZGT7Js',
    'port':3306,
}
