import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from crawlspider.items import Content
from lxml import etree

class BiqgSpider(CrawlSpider):
    name = 'biqg'         # 爬虫名称
    allowed_domains = ['bbiquge.net']          # 允许爬取的域名
    start_urls = ['https://www.bbiquge.net/book_872/']            # 起始抓取地址
    
    link_extractor1 = LinkExtractor(allow=r'[0-9]+\.html', restrict_xpaths='/html/body/div[4]/dl/dd[1]/a')      # 抓取小说简介页面的第一章链接
    link_extractor2 = LinkExtractor(restrict_xpaths='//*[@id="link-next"]')         # 抓取章节内容中“下一章”的链接
    
    # Rule 对象的集合，每一个实例都定义了一种采集站点的行为
    rules = (
        Rule(link_extractor1, callback='parse_item', follow=True),
        Rule(link_extractor2, callback='parse_item', follow=True),
    )
    # 第一个 Rule 抓取简介页面并跟进到小说开始章节
    # 第二个 Rule 抓取章节内容并跟进到下一章节，直至结束
    
    book = ''             # 存储小说文件名的字符串类型属性
    
    # parse_start_url 方法用于爬取起始响应，处理 parse（默认回调函数） 返回的 response；这里 parse_start_url 方法处理第一个 Rule 和 第二个 Rule 开始爬取时 Resquest 方法返回的 response
    # 因为 CrawlSpider 的 _requests_to_follow 方法，接下来符合 Rule 的 link 的回调函数被指定为 _response_downloaded 方法
    def parse_start_url(self,response):
        html = response.text
        html_obj = etree.HTML(html)
        
        if BiqgSpider.book == '':           # 处理第一个 Rule 的起始响应，创建小说文本文件
            str = html_obj.xpath(
                '//*[@id="info"]/h1/text()'
            )[0]
            
            str = str.replace(' ','')
        
            BiqgSpider.book = "{0}.txt"\
                .format(str)
        
            with open(BiqgSpider.book, 'wb') as file:
                print(BiqgSpider.book + " 文件创建成功")
            yield []
        
        if BiqgSpider.book != '':          # 处理第二个 Rule 的起始响应，存储小说起始章节的内容
            content = Content()
            content["chapter"] = html_obj.xpath(
                '//*[@id="main"]/h1/text()'
            )
            content["full_text"] = html_obj.xpath(
                '//*[@id="content"]/text()'
            )
            yield content
        

    def parse_item(self, response):                 # 两个 Rule 的 callback 函数，处理符合 Rule 规则的 link 的 response
        html = response.text
        html_obj = etree.HTML(html)
        
        content = Content()
        
        content["chapter"] = html_obj.xpath(            # 提取章节标题
            '//*[@id="main"]/h1/text()'
        )
        content["full_text"] = html_obj.xpath(          # 提取文本内容
            '//*[@id="content"]/text()'
        )
        yield content