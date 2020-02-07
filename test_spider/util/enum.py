from enum import Enum, unique

@unique
class CrawlType(Enum):

    scrapy = 'scrapy' # normal

    selenium = 'selenium'

    puppeeter = 'puppeeter'
