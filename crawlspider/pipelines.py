# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from crawlspider.items import Content

from crawlspider.spiders.biqg import BiqgSpider    # 导入爬虫类

class CrawlspiderPipeline:
    def process_item(self, item, spider):
        return item

class BiqgPipeline(object):
    def __init__(self):           # 类实例化的初始化
        self.fp = None
    
    def open_spider(self, spider):         # 启动爬虫时执行
        print("启动爬虫")
        
    def process_item(self, item, spider):        # 处理提取到的数据
        if self.fp == None:
            try:
                self.fp = open(BiqgSpider.book, 'wb')       # 以二进制追加模式打开文件，文件名为 BiqgSpider 类的字符串属性
                print("文件打开成功")
            except Exception as e:
                print(e)
        else:
            if len(item["chapter"]) != 0:                  # 判断是否由章节标题，如果有，整理字符串后写入小说文本文件
                str = item["chapter"][0]
                str = str.replace('。', '')
                self.fp.write((str+'\n\n').encode(encoding='utf-8'))        # 以 utf-8 编码格式写入小说文本
            
            for str in item["full_text"]:           # 在循环中处理字符串并写入小说文件
                if str == item["full_text"][0] or str == item["full_text"][1]:        # 内容固定的广告，不写入文件
                    continue
                str = str.replace('\xa0\xa0',' ')
                self.fp.write((str+'\n\n').encode(encoding='utf-8'))      
    
    def close_spider(self, spider):       # 关闭爬虫时执行，关闭文件防止资源浪费
        self.fp.close()
        print("关闭爬虫")