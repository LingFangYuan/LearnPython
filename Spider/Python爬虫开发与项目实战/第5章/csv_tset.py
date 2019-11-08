import csv
from collections import namedtuple


headers = ['ID', 'UserName', 'Password', 'age', 'country']
rows = [(1001, 'qiye', 'qiye_pass', 24, 'China'),
        (1002, 'Mary', 'Mary_pass', 20, 'USA'),
        (1003, 'Jack', 'Jack_pass', 20, 'USA')]

with open('qiye.csv', 'w', newline='', encoding='utf-8') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(rows)

with open('qiye.csv', 'r', encoding='utf-8') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    print(headers)
    for row in f_csv:
        print(row)

with open('qiye.csv', 'r', encoding='utf-8') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    Row = namedtuple('Row', headers)
    for r in f_csv:
        row = Row(*r)
        print(row.UserName, row.Password)
        print(row)

with open('qiye.csv', 'r', encoding='utf-8') as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
        print(row.get('UserName'), row.get('Password'))
        
