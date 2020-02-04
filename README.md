# TF-TestBySpider

Test framework based on spider-crawler/ocr/headless browser

基于爬虫检测、图像识别、无头浏览器的测试框架

## Requirements
`python3.8` + `scrapy1.8` + `peewee3.13.1`

## 工程目录结构
```shell
.
├── README.md
├── __init__.py
├── requirements.txt
├── run.py
├── test_spider
│   ├── __init__.py
│   ├── commands
│   │   ├── __init__.py
│   │   └── crawlall.py
│   ├── db
│   │   ├── __init__.py
│   │   ├── spider_db.py                # 数据操作类
│   │   └── spider_db_model.py          # 数据模型类
│   ├── items.py                        # pipelines的item对象                       
│   ├── middlewares.py
│   ├── pipelines.py                    # 管道处理逻辑
│   ├── settings.py                     # 全局配置
│   ├── spiders
│   │   ├── __init__.py
│   │   └── aliyun_product_spider.py
│   └── util                            # 工具类        
│       ├── __init__.py
│       ├── constant.py
│       ├── counter.py                  # 计数器
│       ├── global_pram.py
│       └── print_format_util.py
└── scrapy.cfg                          # 根配置
```
## Installation
```shell
> pip3 install scrapy  peewee
```

* 本地运行爬虫检测例子:
<pre>scrapy crawl aliyun_product_spider</pre>
* 本地运行所有例子:
<pre>scrapy crawlall </pre>

