import time

from HtmlDownloader import HtmlDownloader
from HtmlParser import HtmlParser
from DataOutput import DataOutput

class SpiderMan:

    def __init__(self):
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()
        self.output = DataOutput()

    def crawl(self, root_url):
        if root_url is None:
            return
        content = self.downloader.download(root_url)
        urls = self.parser.parser_url(root_url, content)
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            try:
                r_url = url[0]
                t = time.strftime('%Y%m%d%H%M%S' ,time.localtime()) + '338518'
                argument0 = url[1]
                rank_url = 'http://service.library.mtime.com/Movie.api?' + \
                'Ajax_CallBack=true' + \
                '&Ajax_CallBackType=Mtime.Library.Services' + \
                '&Ajax_CallBackMethod=GetMovieOverviewRating' + \
                '&Ajax_CrossDomain=1' + \
                '&Ajax_RequestUrl=%s' + \
                '&t=%s' + \
                '&Ajax_CallBackArgument0=%s' 
                rank_url = rank_url % (r_url, t, argument0)
                # print(rank_url)
                jsons = self.downloader.download(rank_url)
                data = self.parser.parser_json(rank_url, jsons)
                if data:
                    self.output.store_data(data)
            except Exception as e:
                raise
                print('Crawl failed')
        self.output.output_end()
        print('Crawl finish!')


if __name__ == '__main__':
    spider = SpiderMan()
    spider.crawl('http://theater.mtime.com/China_Beijing/')

