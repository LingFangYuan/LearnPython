# -*- coding: utf-8 -*-
import os
import re
import json
from http import cookiejar

import scrapy
from requests.utils import dict_from_cookiejar
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from zhihuCrawl.items import UserInfoLoader, UserInfoItem, RelationItem


class ZhihuComSpider(scrapy.Spider):
    name = 'zhihu.com'
    allowed_domains = ['zhihu.com']
    start_urls = [
        'https://www.zhihu.com/people/xiao-lou-yi-ye-ting-chun-yu-74-69']
    cookies_path = './cookies.txt'

    def start_requests(self):
        def load_cookies():
            cs = cookiejar.LWPCookieJar(self.cookies_path)
            try:
                cs.load(ignore_discard=True)
            except FileNotFoundError:
                cs.save()
            return dict_from_cookiejar(cs)

        url = 'https://www.zhihu.com/signin'
        cookies = load_cookies()
        return [scrapy.Request(url=url, callback=self.login, cookies=cookies)]

    def login(self, response):
        if 'sigin' in response.url:
            print('登录失败！')
            return
        return scrapy.Request(url=self.start_urls[0], callback=self.parse_user_info)

    def parse_user_info(self, response):
        '''
        解析用户信息
        :param response:
        :return:
        '''
        l = UserInfoLoader(item=UserInfoItem(), response=response)
        user_id = os.path.split(response.url)[-1]
        l.add_value('user_id', user_id)
        l.add_xpath(
            'user_image_url', './/img[@class="Avatar Avatar--large UserAvatar-inner"]/@src')
        l.add_xpath(
            'name', './/h1[@class="ProfileHeader-title"]/span[1]/text()')
        l.add_xpath(
            'business', './/div[@class="ProfileHeader-infoItem" and position()=1]/text()[1]')
        l.add_xpath('gender', './/svg[@class="Icon Icon--male"]/@class')
        l.add_xpath('gender', './/svg[@class="Icon Icon--female"]/@class')
        l.add_xpath(
            'employment', './/div[@class="ProfileHeader-infoItem" and position()=1]/text()[2]')
        l.add_xpath(
            'position', './/div[@class="ProfileHeader-infoItem" and position()=1]/text()[3]')
        l.add_xpath(
            'education', './/div[@class="ProfileHeader-infoItem" and position()=2]/text()[1]')
        l.add_xpath(
            'followees_num', './/div[@class="NumberBoard-itemInner" and div="关注了"]/strong/text()')
        l.add_xpath(
            'followers_num', './/div[@class="NumberBoard-itemInner" and div="关注者"]/strong/text()')
        relation_url = response.xpath(
            './/a[@class="Button NumberBoard-item Button--plain"]/@href').extract()

        yield l.load_item()

        for url in relation_url:
            if 'following' in url:
                relation_type = 'following'
            else:
                relation_type = 'followers'
            relation_id = list()
            relation_url = list()
            yield scrapy.Request(url=response.urljoin(url), callback=self.parse_relation,
                                 meta={'user_id': user_id,
                                       'relation_type': relation_type,
                                       'relation_id': relation_id,
                                       'relation_url': relation_url,
                                       'page_num': 1})

    def parse_relation(self, response):
        user_id = response.meta['user_id']
        relation_type = response.meta['relation_type']
        relation_id = response.meta['relation_id']
        relation_url = response.meta['relation_url']
        page_num = response.meta['page_num']
        try:
            json_str = response.xpath(
                './/*[@id="js-initialData"]/text()').extract()[0]
            js = json.loads(json_str)
            follow = {k: v['url'] for k, v in js['initialState']['entities'][
                      'users'].items() if v.get('url') and k != user_id}
            relation_id.extend(follow.keys())
            relation_url.extend(follow.values())
        except:
            pass

        # 爬取下一页
        next_button = response.xpath(
            './/*[@class="Pagination"]/button[contains(text(), "下一页")]').extract()
        curr_page = response.xpath(
            './/*[@class="Pagination"]/button[@class="Button PaginationButton PaginationButton--current Button--plain"]/text()').extract()
        if next_button and page_num <= 2:
            base_url = re.findall(r'^[^?]*', response.url)[0]
            page_num = int(curr_page[0]) + 1
            next_url = base_url + '?page=' + str(page_num)
            yield scrapy.Request(url=next_url, callback=self.parse_relation,
                                 meta={'user_id': user_id,
                                       'relation_type': relation_type,
                                       'relation_id': relation_id,
                                       'relation_url': relation_url,
                                       'page_num': page_num})
        else:
            item = RelationItem(user_id=user_id, relation_type=relation_type,
                                relation_id=relation_id)
            yield item
            for url in relation_url:
                yield scrapy.Request(url=url, callback=self.parse_user_info)
