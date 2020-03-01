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

CONST.ALI_YUN_WEB_SPIDER_NAME = 'ali_web_spider'

CONST.ALI_YUN_M_URL = 'https://m.aliyun.com'

CONST.ALI_YUN_M_SPIDER_NAME = 'ali_m_spider'

CONST.WU_BA_M_URL = 'https://m.58.com'

CONST.ALI_YUN_M_P_SPIDER_NAME = 'ali_m_p_spider'

CONST.ALI_YUN_HEADER = {
    'Content-type': 'application/json; charset=utf-8',
}

CONST.PIC_PATH = 'test_spider/pic'

CONST.CHROME_DRIVER_BIN_PATH = 'test_spider/bin/chromedriver'

CONST.CHROME_DRIVER_OPTIONS = [
    "start-maximized",
    "enable-automation",
    "--headless",
    "--no-sandbox",
    "--disable-infobars",
    '--disable-dev-shm-usage',
    "--disable-browser-side-navigation",
    "--disable-gpu",
    "--disable-extensions",
    "--dns-prefetch-disable",
]

CONST.CHROME_DRIVER_PAGE_LOAD_TIMEOUT = 200

CONST.SPIDER_DB_INFO = {
    'database': 'hanlingzhi',
    'host': 'localhost',
    'user': 'hanlingzhi',
    'password': '123456',
    'port':3306,
}
