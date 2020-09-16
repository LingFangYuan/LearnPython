import hashlib

from scrapy.utils.url import canonicalize_url
from scrapy.dupefilters import RFPDupeFilter
from pybloom_live import ScalableBloomFilter

class URLBloomFilter(RFPDupeFilter):
    '''根据urlhash_bloom过滤'''
    def __init__(self, path=None):
        self.url_sbf = ScalableBloomFilter(mode=ScalableBloomFilter.SMALL_SET_GROWTH)
        super().__init__(path)

    def request_seen(self, request):
        fp = hashlib.sha1()
        fp.update(canonicalize_url(request.url))
        url_sha1 = fp.hexdigest()
        if url_sha1 in self.url_sbf:
            return True
        else:
            self.url_sbf.add(url_sha1)
