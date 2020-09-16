from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from zhihuCrawl.spiders.zhihu_com import ZhihuComSpider


if __name__ == '__main__':
    process = CrawlerProcess(get_project_settings())
    # process.crawl('cnblogs')
    process.crawl('zhihu.com')
    process.start()
