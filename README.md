# crawlspider
这是一个使用 scrapy 框架写的爬虫，是我学习 scrapy 中 crawlspider 类的一个实例。

## 功能
抓取[笔趣阁](https://www.bbiquge.net/)网站的小说，存储为 txt 文本格式。

<br>

## 使用方法
1、项目依赖 scrapy 框架，首先下载包。
```txt
pip3 install scrapy
```

验证 scrapy 下载：
```txt
scrapy --version
```

2、打开项目文件夹，打开 spiders 文件夹下的 biqg.py 文件。这是 crawlspider 项目的爬虫文件，在 BiqgSpider 类的 start_ urls 属性里，指向了要爬取的小说简介页面，链接格式为 `https://www.bbiquge.net/book_[0-9]+/`。

3、在 start_urls