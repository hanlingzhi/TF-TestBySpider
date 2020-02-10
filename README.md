# TF-TestBySpider

Test framework based on spider-crawler/ocr/headless browser

基于爬虫检测、图像识别、无头浏览器的测试框架

## Requirements
`
selenium==3.141.0
Scrapy==1.8.0
syncer==1.3.0
opencv_python==4.2.0.32
peewee==3.13.1
scikit_image==0.16.2
imutils==0.5.3
pyppeteer==0.0.25
Pillow==7.0.0
skimage==0.0
`

## 工程目录结构
```shell
.
├── README.md
├── __init__.py
├── requirements.txt
├── scrapy.cfg                          # 根配置
└── test_spider
    ├── __init__.py
    ├── bin
    │   └── chromedriver
    ├── commands
    │   ├── __init__.py
    │   └── crawlall.py
    ├── items.py                        # item对象
    ├── middlewares.py                  # 中间件处理逻辑
    ├── orm
    │   ├── __init__.py
    │   ├── spider_db.py
    │   └── spider_db_model.py
    ├── pic
    │   └── __init__.py
    ├── pipelines.py                    # 管道处理逻辑
    ├── request
    │   ├── puppeeter_request.py        # request封装
    │   └── selenium_request.py
    ├── settings.py                     # 全局配置
    ├── spiders                         # 爬虫
    │   ├── __init__.py
    │   ├── aliyun_m_p_spider.py
    │   ├── aliyun_m_spider.py
    │   ├── aliyun_product_spider.py
    │   └── aliyun_product_web_spider.py
    └── util
        ├── __init__.py
        ├── constant.py
        ├── counter.py                  # 计数器
        ├── enum.py
        ├── file.py
        ├── global_pram.py
        ├── opencv_img_ssim.py          # opencv
        ├── pil_img_ssim.py
        └── print_format_util.py
```
## Installation
* chromedriver根据浏览器版本需要单独下载, 可以访问 https://npm.taobao.org/mirrors/chromedriver 下载
* pyppeeter的运行额外需要安装ssl认证
```shell
> sudo /Applications/Python\ 3.8/Install\ Certificates.command
```
## RUN
* 运行接口爬虫检测例子(scrapy + peewee):
<pre>scrapy crawl ali_product_spider</pre>
* 运行URL遍历+图像比对爬虫检测例子(scrapy + selenium(headless) + PIL):
<pre>scrapy crawl ali_web_spider</pre>
* 运行M页面+图像比对爬虫检测例子(scrapy + selenium(headless） + PIL/OpenCV):
<pre>scrapy crawl ali_m_spider</pre>
* 运行M页面+图像比对爬虫检测例子(scrapy + pyppeeter + PIL/OpenCV):
<pre>scrapy crawl ali_m_p_spider</pre>
* 本地运行所有例子:
<pre>scrapy crawlall </pre>

