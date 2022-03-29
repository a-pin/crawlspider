# crawlspider
这是一个使用 scrapy 框架写的爬虫，基于 crawlspider 类。

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

2、打开项目文件夹，打开 spiders 文件夹下的 biqg.py 文件。这是 crawlspider 项目的爬虫模块，在 BiqgSpider 类的 start_ urls 属性里，指向了要爬取的小说简介页面，链接格式为 `https://www.bbiquge.net/book_[0-9]+/`。

3、把 start_urls 中的起始爬取链接修改为自己想要爬取的小说的简介页面链接。

4、启动爬虫，爬虫会自动爬取小说，并将内容保存在与小说同名的 txt 文件下。

<br>

## 注意
源码中附有注释，如果你刚刚学习 scrapy 框架，看看源码注释会有一点益处。

由于此项目爬虫依赖于精确的 XPath 定位，如遇网站前端代码变更，可能会造成爬取失败，你可以新建问题要求我更新代码，也可以发起 pull request。我会尽快处理。

**此 scrapy 项目仅作为个人学习所用，任何人不得以商业目的来使用它爬取小说！**