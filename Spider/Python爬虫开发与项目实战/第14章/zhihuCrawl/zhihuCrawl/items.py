# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, Identity, Compose


def determine_gender(value):
    if 'female' in value:
        return '女'
    return '男'


class ZhihucrawlItem(scrapy.Item):
    # define the fields for your item here like:
    pass


class UserInfoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # id
    user_id = scrapy.Field()
    # 头像 img
    user_image_url = scrapy.Field()
    # 姓名
    name = scrapy.Field()
    # 技术领域
    business = scrapy.Field()
    # 性别
    gender = scrapy.Field()
    # 公司
    employment = scrapy.Field()
    # 职位
    position = scrapy.Field()
    # 教育经历
    education = scrapy.Field()
    # 我关注的人数
    followees_num = scrapy.Field()
    # 关注我的人数
    followers_num = scrapy.Field()


class RelationItem(scrapy.Item):

    # 用户id
    user_id = scrapy.Field()
    # relation 类型
    relation_type = scrapy.Field()
    # 和我有关系的人的id列表
    relation_id = scrapy.Field()


class UserInfoLoader(ItemLoader):
    default_output_processor = TakeFirst()

    gender_out = Compose(TakeFirst(), determine_gender)
    followees_num_out = Compose(TakeFirst(), lambda x: x.replace(',', ''), int)
    followers_num_out = Compose(TakeFirst(), lambda x: x.replace(',', ''), int)
