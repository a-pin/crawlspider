# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
    
class Content(scrapy.Item):            # 存储章节标题和内容
    chapter = scrapy.Field()
    full_text = scrapy.Field()
