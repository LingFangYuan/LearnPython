import urllib.request
import re
from urllib.error import URLError, HTTPError, ContentTooShortError


def download(url, user_agent='wswp', num_retries=2, charset='utf-8', proxy=None):
    print('Downloading:', url)
    request = urllib.request.Request(url)
    request.add_header('User-agent', user_agent)
    try:
        if proxy:
            proxy_support = urllib.request.ProxyHandler({'http': proxy})
            opener = urllib.request.build_opener(proxy_support)
            urllib.request.install_opener(opener)
        resp = urllib.request.urlopen(request)
        cs = resp.headers.get_content_charset()
        if not cs:
            cs = charset
        html = resp.read().decode(cs)
    except (URLError, HTTPError, ContentTooShortError) as e:
        print('Download error:', e.reason)
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                return download(url, user_agent=user_agent, num_retries=num_retries - 1, charset=charset, proxy=proxy)
    return html


def crawl_sitemap(url):
    sitemap = download(url)
    links = re.findall(r'<loc>(.*?)</loc>', sitemap)
    print(links)
    # for link in links:
    #     html = download(link)


if __name__ == '__main__':
    print(crawl_sitemap('http://example.python-scraping.com/sitemap.xml'))
