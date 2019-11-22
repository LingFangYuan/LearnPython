import pymysql


try:
    con = pymysql.connect(host='172.30.196.104', user='root',
                          password='111111', db='test', port=3306)
    cur = con.cursor()
    # rs = cur.execute('insert into student(name, sex, age) values(%s, %s, %s)',
    #                 ('ling', '男', 26))
    # con.commit()
    cur.execute('select * from student')
    rs = cur.fetchall()
    fields = tuple(f[0] for f in cur.description)
    print(fields)
    for line in rs:
        print(line)

finally:
    cur.close()
    con.close()
