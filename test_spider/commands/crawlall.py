from scrapy.commands import ScrapyCommand

class Command(ScrapyCommand):

    requires_project = True

    def syntax(self):
        return '[options]'

    def short_desc(self):
        return 'Runs all of ahs the spiders'

    def run(self, args, opts):
        spider_list = self.crawler_process.spider_loader.list()
        for name in spider_list:
            if str(name).startswith("ali"):
                self.crawler_process.crawl(name, **opts.__dict__)
        self.crawler_process.start()