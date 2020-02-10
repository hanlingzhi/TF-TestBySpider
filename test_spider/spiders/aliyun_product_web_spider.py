import scrapy, os, time
from PIL import Image

from test_spider.request.selenium_request import SeleniumRequest
from test_spider.util.constant import CONST
from test_spider.orm import spider_db
from test_spider.util.print_format_util import PrintFormatUtil
from test_spider.util.enum import CrawlType
from test_spider.util.file import FileUtil
from test_spider.util.pil_img_ssim import ImageSSIM
from test_spider.util.opencv_img_ssim import OpenCVSSIM

__author__ = 'hanlingzhi'

'''
create_date:
    2019.7.30
usage: 
    阿里云产品业务页面截屏比对
'''


class ALIProductWebDiffSpider(scrapy.Spider):

    name = CONST.ALI_YUN_WEB_SPIDER_NAME  # 定义爬虫名

    allowed_domains = [CONST.ALI_YUN_DOMAIN]  # 接受处理的域名

    crawl_type = CrawlType.selenium

    link_list = spider_db.get_product_url_all()

    def start_requests(self):
        for service_name, service_url in self.link_list.items():
            PrintFormatUtil.print_line("检查{}的页面, url {}".format(service_name, service_url))
            args_dict = {'title': service_name}
            yield SeleniumRequest(url=service_url, callback=self.parse, screen_shot=True, wait_time=20,
                                  r_dict=args_dict)

    def parse(self, response):
        service_pic_path = os.path.join(CONST.PIC_PATH, response.meta['r_dict']['title'])
        os.makedirs(service_pic_path, exist_ok=True)
        current_time = str(int(time.time()))
        service_pic_name = os.path.join(service_pic_path, current_time + ".png")
        service_pic_small_name = os.path.join(service_pic_path, current_time + "_s.png")
        service_pic_diff_name = os.path.join(service_pic_path, current_time + "_diff.png")
        service_pic_oc_diff_name = os.path.join(service_pic_path, current_time + "_oc_diff.png")
        PrintFormatUtil.print_line("pic save path {}".format(service_pic_name))
        with open(service_pic_name, 'wb') as image_file:
            image_file.write(response.meta['screen_shot'])

        # 设置图片压缩
        image = Image.open(service_pic_name)
        w,h  = image.size
        PrintFormatUtil.print_line("原有图片大小 width {} height {}".format(w,h))
        d_img = image.resize((int(w/2),int(h/2)),Image.ANTIALIAS)
        w, h = d_img.size
        PrintFormatUtil.print_line("处理后的图片大小 width {} height {}".format(w, h))
        d_img.save(service_pic_small_name, quality=95)
        del response, image

        # 读取latest文件
        latest_path = os.path.join(service_pic_path, 'latest')
        if os.path.exists(latest_path) and os.path.isfile(latest_path):
            with open(latest_path, 'r') as f:
                old_file_info = f.read()
            old_file_info = old_file_info.split(" ")
            old_file_info_name = old_file_info[0]
            old_file_info_md5 = old_file_info[1]
            old_service_pic_name = os.path.join(service_pic_path, old_file_info_name)
            PrintFormatUtil.print_line("old pic path {}".format(old_service_pic_name))
            if old_file_info_md5 == FileUtil.get_md5(old_service_pic_name):
                PrintFormatUtil.print_line("比对图片 {} | {}".format(service_pic_small_name, old_file_info_name))
                # 比对图片(PIL和OPENCV两种模式)
                iss = ImageSSIM(service_pic_small_name, old_service_pic_name, service_pic_diff_name)
                o_iss = OpenCVSSIM(service_pic_small_name, old_service_pic_name, service_pic_oc_diff_name)
                pil_s_code = iss.compare_images()
                oc_s_code = o_iss.compare_images()
                PrintFormatUtil.print_line("PIL库两者的相似度: {}".format(pil_s_code))
                PrintFormatUtil.print_line("OPEN_CV库两者的相似度: {}".format(oc_s_code))
                # 这个值可以设置(0-1),  1 非常严格
                if pil_s_code < 1 and oc_s_code < 1:
                    iss.output_diff()
                    o_iss.output_diff()
            else:
                PrintFormatUtil.print_line("old pic md5 error. new {} old {}".format(
                    FileUtil.get_md5(old_service_pic_name),old_file_info_md5))
        # 重新生成latest文件
        with open(latest_path, "w") as file:
            file.write(os.path.basename(service_pic_small_name) + " " + FileUtil.get_md5(service_pic_small_name))
