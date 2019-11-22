import time

import pymysql


class DataOutput:

    def __init__(self):
        self.datas = []
        self._init_db()
        self.create_table('Mtime')
        self.date = time.strftime('%Y-%m-%d %X',time.localtime())

    def _init_db(self):
        '''
        初始化数据库连接
        '''
        self.con = pymysql.connect(host='localhost', user='root',
                                   password='111111', db='test', port=3306)
        self.cur = self.con.cursor()

    def _close(self):
        self.cur.close()
        self.con.close()

    def _re_init(self):
        try:
            self.cur.ping()
        except:
            self._init_db()

    def create_table(self, table_name):
        '''
        创建存储数据的表
        :params table_name: 创建的表名
        :return:
        '''
        values = '''
            date datetime comment "爬取时间",
            MovieId integer comment "电影ID",
            movieTitle varchar(255) comment "电影名称",
            RatingFinal float comment "综合评分",
            RDirectorFinal float comment "导演评分",
            RPictureFinal float comment "画面评分",
            RStoryFinal float comment "故事评分",
            ROtherFinal float comment "音乐评分",
            Mrank integer comment "排名",
            ShowDays integer comment "上映时间",
            TotalBoxOffice varchar(255) comment "总票房",
            TodayBoxOffice varchar(255) comment "今日票房",
            isRelease integer comment "上映类型，0 未上映，1 正在上映，2 即将上映"
        '''

        self._re_init()

        try:
            r = self.cur.execute(
                'create table if not exists %s( %s )' % (table_name, values))
            self.table_name = table_name
            print('创建表: %s 成功！' % table_name)
        except Exception as e:
            print(e)
            print('创建表: %s 失败！' % table_name)
            self._close()
            raise

    def store_data(self, data):
        '''
        缓存数据，大于10条时存储到数据库中

        '''
        if data is None:
            return
        self.datas.append(data)
        if len(self.datas) >= 10:
            self.output_db(self.table_name)

    def output_db(self, table_name):
        '''
        保存数据到数据库
        '''
        sql = '''insert into %s
            (date, MovieId, movieTitle, RatingFinal, RDirectorFinal,
            RPictureFinal, RStoryFinal, ROtherFinal, Mrank,
            ShowDays , TotalBoxOffice, TodayBoxOffice, isRelease)
            values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''' % table_name

        self._re_init()

        try:
            
            for data in self.datas:
                print(data)
                self.cur.execute(sql.replace('?', '%s') , (self.date, ) + data)
            self.con.commit()
            self.datas.clear()
            print('成功插入10条记录!')
        except Exception as e:
            print(e)
            print('插入记录出现异常!')
            self.con.rollback()
            self._close()

    def output_end(self):
        if len(self.datas) > 0:
            self.output_db(self.table_name)
        self._close()

if __name__ == '__main__':
    output = DataOutput()
    data = (None, None, None, None, None, None,
            None, None, None, None, None, None)
    for i in range(10):
        output.store_data(data)
    del output
