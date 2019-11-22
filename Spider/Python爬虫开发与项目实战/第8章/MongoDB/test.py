import datetime

import pymongo


client = pymongo.MongoClient()
db = client.papers
collection = db.books

book = {'author': 'Mike',
        'text': 'My first book!',
        'tags': ['爬虫', 'python', '网络'],
        'date': datetime.datetime.now()
        }
# # 插入文档
# book_id = collection.insert_one(book)
# print(book_id)

# # 更新文档
# collection.update_many({'author': 'Mike'}, {'$set': {'test': '1python book'}})

# 删除文档
collection.delete_one({'author': 'Mike'})

# 查询文档
rs = collection.find({'author': 'Mike'})
for line in rs:
    print(line)
