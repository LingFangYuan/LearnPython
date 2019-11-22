import re
import json


class HtmlParser:

    def parser_url(self, page_url, content):
        '''
        解析网页中待爬取的URL
        :params page_url: 爬取网页的URL
        :params content: 网页的内容
        :return: 返回去重后的URL列表
        '''
        pattern = re.compile(r'(http://movie.mtime.com/(\d+?)/)')
        urls = pattern.findall(content)
        if urls is not None:
            return list(set(urls))
        return None

    def parser_json(self, page_url, content):
        '''
        解析动态链接返回的json串
        :params page_url: 爬取动态链接的URL
        :params content: 动态链接返回的内容
        :return: 返回提取到的指定数据元组
        '''
        pattern = re.compile(r'=(.*?);')
        jsons = pattern.findall(content)[0]
        if jsons is not None:
            result = json.loads(jsons)
            try:
                value = result['value']
                isRelease = value['isRelease']
            except Exception as e:
                print(e)
                return None
            if isRelease:
                if value.get('boxOffice') is not None:
                    release_type = 1
                else:
                    release_type = 2
            else:
                release_type = 0

            return self._parser_release(page_url, value, release_type)
        return None

    def _parser_release(self, page_url, value, release_type=0):
        '''
        提取json中的指定内容
        :params page_url: 爬取动态链接的URL
        :params value: 动态链接返回的json
        :params release_type: 上映类型，1 已上映；2 即将上映；0 还有很久上映
        :return: 返回提取到的指定数据元组
        '''
        try:
            isRelease = release_type

            movieRating = value.get('movieRating')
            MovieId = movieRating.get('MovieId')
            movieTitle = value.get('movieTitle')
            RatingFinal = movieRating.get('RatingFinal')
            RDirectorFinal = movieRating.get('RDirectorFinal')
            RPictureFinal = movieRating.get('RPictureFinal')
            RStoryFinal = movieRating.get('RStoryFinal')
            ROtherFinal = movieRating.get('ROtherFinal')

            boxOffice = value.get('boxOffice')
            hotValue = value.get('hotValue')
            try:
                rank = boxOffice.get('Rank')
                TotalBoxOffice = boxOffice.get('TotalBoxOffice')
                TotalBoxOfficeUnit = boxOffice.get('TotalBoxOfficeUnit')
                TodayBoxOffice = boxOffice.get('TodayBoxOffice')
                TodayBoxOfficeUnit = boxOffice.get('TodayBoxOfficeUnit')
                ShowDays = boxOffice.get('ShowDays')
            except:
                rank = hotValue.get('Ranking') if hotValue is not None else 0
                TotalBoxOffice = '无'
                TotalBoxOfficeUnit = ''
                TodayBoxOffice = '无'
                TodayBoxOfficeUnit = ''
                ShowDays = 0

            return (MovieId, movieTitle, RatingFinal, RDirectorFinal,
                    RPictureFinal, RStoryFinal, ROtherFinal, rank, ShowDays,
                    TotalBoxOffice + TotalBoxOfficeUnit, TodayBoxOffice + TodayBoxOfficeUnit,
                    isRelease)

        except Exception as e:
            print(e, page_url, value)
            return None
