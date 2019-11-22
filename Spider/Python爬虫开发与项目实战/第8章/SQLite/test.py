import sqlite3

try:
    con = sqlite3.connect('test.db')
    cur = con.cursor()
    # cur.executemany('insert into person values(?, ?, ?)', [(2, 'marry', 20), (5, 'jack', 20)])
    # con.commit()
    cur.execute('select * from person')
    for row in cur.fetchall():
        print(row)
finally:
    cur.close()
    con.close()
