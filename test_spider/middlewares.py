# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import time

from scrapy import signals
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from scrapy.http import HtmlResponse
from test_spider.util.constant import CONST
from test_spider.util.print_format_util import PrintFormatUtil
from test_spider.request.selenium_request import SeleniumRequest


class TestSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class TestSpiderDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    driver = None

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        PrintFormatUtil.print_line("重新定义crawler-spider")
        s = cls()
        # 绑定节点的监听事件
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        crawler.signals.connect(s.spider_closed, signal=signals.spider_closed)
        return s

    def process_request(self, request, spider):
        PrintFormatUtil.print_line("spider {} : 开始处理 Request".format(spider.name))
        if spider.crawl_type.value == 'selenium' and isinstance(request, SeleniumRequest):
            self.driver.set_window_size(800, 600)
            self.driver.get(request.url)
            # copy cookie
            for cookie_name, cookie_value in request.cookies.items():
                self.driver.add_cookie(
                    {
                        'name': cookie_name,
                        'value': cookie_value
                    }
                )
            if request.wait_until:
                WebDriverWait(self.driver, request.wait_time).until(request.wait_until)
            if request.screen_shot:
                # Get the actual page dimensions using javascript
                width = self.driver.execute_script(
                    "return Math.max(document.body.scrollWidth, document.body.offsetWidth, "
                    "document.documentElement.clientWidth, document.documentElement.scrollWidth, "
                    "document.documentElement.offsetWidth);")
                height = self.driver.execute_script(
                    "return Math.max(document.body.scrollHeight, document.body.offsetHeight, "
                    "document.documentElement.clientHeight, document.documentElement.scrollHeight, "
                    "document.documentElement.offsetHeight);")
                # resize
                PrintFormatUtil.print_line("reset size {}:{}".format(width, height))
                self.driver.set_window_size(width, height)
                time.sleep(1)
                request.meta['screen_shot'] = self.driver.get_screenshot_as_png()
            if request.script:
                self.driver.execute_script(request.script)
            request.meta['r_dict'] = request.r_dict
            body = str.encode(self.driver.page_source)
            # Expose the driver via the "meta" attribute
            request.meta.update({'driver': self.driver})
            return HtmlResponse(
                self.driver.current_url,
                body=body,
                encoding='utf-8',
                request=request
            )
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        PrintFormatUtil.print_line("spider {} : 开始处理 Response".format(spider.name))
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        PrintFormatUtil.print_line("spider {} : 开始处理".format(spider.name))
        PrintFormatUtil.print_line("spider {} , 运行模式 {}".format(spider.name, spider.crawl_type.value))
        if spider.crawl_type.value == 'selenium':
            chrome_options = Options()
            list([chrome_options.add_argument(x) for x in CONST.CHROME_DRIVER_OPTIONS])
            self.driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=CONST.CHROME_DRIVER_BIN_PATH)

    def spider_closed(self, spider):
        """Shutdown the driver when spider is closed"""
        PrintFormatUtil.print_line("spider {} : 结束处理".format(spider.name))
        if spider.crawl_type.value == 'selenium' and not self.driver is None:
            PrintFormatUtil.print_line("spider {} : selenium driver 销毁".format(spider.name))
            self.driver.close()
            self.driver.quit()
