import scrapy
from scrapy import Selector
from scrapy.spiders import Rule, CrawlSpider, XMLFeedSpider
from scrapy.linkextractors import LinkExtractor
from scrapy.crawler import CrawlerProcess
from cnblogSpider.items import CnblogspiderItem


# class CnblogsSpider(scrapy.Spider):

#     name = 'cnblogs'  # 爬虫的名称
#     allowed_domains = ['cnblogs.com']  # 允许的域名
#     # 入口URL
#     start_urls = ['https://www.cnblogs.com/qiyeboy/default.html?page=1']

#     def parse(self, response):
#         # 实现网页的解析
#         # 首先抽取所有的文章
#         papers = response.xpath('.//*[@class="day"]')
#         # 从每篇文章中抽取数据
#         for paper in papers:
#             url = paper.xpath(
#                 './/*[@class="postTitle"]/a/@href').extract()[0].strip()
#             title = paper.xpath(
#                 './/*[@class="postTitle"]/a/text()').extract()[0].strip()
#             time = paper.xpath(
#                 './/*[@class="dayTitle"]/a/text()').extract()[0].strip()
#             content = paper.xpath(
#                 './/*[@class="postCon"]/div/text()').extract()[0].strip()
#             item = CnblogspiderItem(
#                 url=url, title=title, time=time, content=content)
#             request = scrapy.Request(url=url, callback=self.parse_body)
#             request.meta['item'] = item  # 将item暂存

#             yield request

#         next_page = response.xpath(
#             './/a[contains(text(), "下一页")]/@href').extract()
#         if next_page:
#             yield scrapy.Request(url=next_page[0], callback=self.parse)

#     def parse_body(self, response):
#         item = response.meta['item']
#         body = response.xpath('.//*[@class="postBody"]')
#         item['image_urls'] = body.xpath('.//img/@src').extract()  # 提取图片链接
#         yield item

class CnblogsSpider(CrawlSpider):

    name = 'cnblogs'  # 爬虫的名称
    allowed_domains = ['cnblogs.com']  # 允许的域名
    # 入口URL
    start_urls = ['https://www.cnblogs.com/qiyeboy/default.html?page=1']
    rules = (Rule(LinkExtractor(allow=(r'/qiyeboy/default.html\?page=\d{1,}',)),
                  follow=True,
                  callback='parse_item'),)

    def parse_item(self, response):
        # 实现网页的解析
        # 首先抽取所有的文章
        papers = response.xpath('.//*[@class="day"]')
        # 从每篇文章中抽取数据
        for paper in papers:
            url = paper.xpath(
                './/*[@class="postTitle"]/a/@href').extract()[0].strip()
            title = paper.xpath(
                './/*[@class="postTitle"]/a/text()').extract()[0].strip()
            time = paper.xpath(
                './/*[@class="dayTitle"]/a/text()').extract()[0].strip()
            content = paper.xpath(
                './/*[@class="postCon"]/div/text()').extract()[0].strip()
            item = CnblogspiderItem(
                url=url, title=title, time=time, content=content)
            request = scrapy.Request(url=url, callback=self.parse_body)
            request.meta['item'] = item  # 将item暂存

            yield request

    def parse_body(self, response):
        item = response.meta['item']
        body = response.xpath('.//*[@class="postBody"]')
        item['image_urls'] = body.xpath('.//img/@src').extract()  # 提取图片链接
        yield item


class XMLSpider(XMLFeedSpider):

    name = 'xmlspider'
    allowed_domains = ['cnblogs.com']
    start_urls = ['http://feed.cnblogs.com/blog/u/269038/rss']
    iterator = 'html'
    itertag = 'entry'

    def adapt_response(self, response):
        return response

    def parse_node(self, response, node):
        print(node.xpath('id/text()').extract()[0])
        print(node.xpath('title/text()').extract()[0])
        print(node.xpath('summary/text()').extract()[0])
