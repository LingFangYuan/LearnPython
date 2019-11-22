from DataOutput import DataOutput
from HtmlDownloader import HtmlDownloader
from HtmlParser import HtmlParser
from UrlManager import UrlManager


class SpiderMan:

    def __init__(self):
        self.manager = UrlManager()
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()
        self.output = DataOutput()

    def crawl(self, root_url):
        # 添加入口URL
        self.manager.add_new_url(root_url)
        # 判断URL管理器中是否有新的URL，同时判断抓取了多少个URL
        while (self.manager.has_new_url() and self.manager.old_url_size() < 100):
            try:
                # 从URL管理器获取新的URL
                new_urls = None
                data = None
                new_url = self.manager.get_new_url()
                # HTML下载器下载网页
                html = self.downloader.download(new_url)
                # HTML解析器抽取网页数据
                new_urls, data = self.parser.parser(new_url, html)
                # 将抽取的url添加到URL管理器中
                self.manager.add_new_urls(new_urls)
                # 数据存储器存储文件
                self.output.sotre_data(data)
                print('已经抓取%s个链接' % self.manager.old_url_size())
            except Exception as e:
                print('crawl failed', e, new_url)
        self.output.output_html()


if __name__ == '__main__':
    spider_man = SpiderMan()
    spider_man.crawl('https://baike.baidu.com/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB')
