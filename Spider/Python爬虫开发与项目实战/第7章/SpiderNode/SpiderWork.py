from multiprocessing.managers import BaseManager

from HtmlDownloader import HtmlDownloader
from HtmlParser import HtmlParser


class QueueManager(BaseManager):
    pass

class SpiderWork:

    def __init__(self):
        # 初始化分布式进程中工作节点的连接工作
        # 实现第一步：使用BaseManager注册用于获取Queue的方法名称
        QueueManager.register('get_url_queue')
        QueueManager.register('get_result_queue')

        # 实现第二步：连接到服务器
        server_addr = '172.30.196.104'
        print('Connect to server %s ...' % server_addr)
        # 注意保持端口和验证口令与服务进程设置的完全一致
        self.m = QueueManager(address=(server_addr, 8001), authkey=b'ling')
        # 网络连接
        self.m.connect()
        # 实现第三步：获取Queue的对象
        self.url_q = self.m.get_url_queue()
        self.result_q = self.m.get_result_queue()
        # 初始化网页下载和解析器
        self.download = HtmlDownloader()
        self.parser = HtmlParser()
        # 发送加入标志到控制节点
        self.result_q.put({'new_urls': 'join', 'data': 'join'})
        print('init finish')

    def crawl(self):
        while True:
            try:
                if not self.url_q.empty():
                    url = self.url_q.get()
                    if url == 'end':
                        print('控制节点通知爬虫节点停止工作...')
                        self.result_q.put({'new_urls': 'end', 'data': 'end'})
                        return
                    print('爬虫节点正在解析: %s' % url)
                    content = self.download.download(url)
                    new_urls, data = self.parser.parser(url, content)
                    self.result_q.put({'new_urls': new_urls, 'data': data})
            except EOFError as e:
                print('连接工作节点失败')
                return
            except Exception as e:
                print(e)
                print('Crawl fali')


if __name__ == '__main__':
    spider = SpiderWork()
    spider.crawl()
