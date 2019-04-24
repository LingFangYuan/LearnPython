bob = ['Bob Smith',  42, 30000, 'Software']
sue = ['Sue Jones', 45, 40000, 'hardware']
people = [bob, sue]
pays = [person[2] for person in people]
pays = map(lambda x: x[2], people)
sum(person[2] for person in people)
people.append(['Tom', 50, 0, None])

NAME, AGE, PAY = range(3)

bob = [['name', 'Bob Smith'], ['age', 42], ['pay', 10000]]
sue = [['name', 'Sue Jones'], ['age', 45], ['pay', 20000]]
people = [bob, sue]

bob = {'name': 'Bob Smith', 'age': 42, 'pay': 30000, 'job': 'dev'}
sue = {'name': 'Sue  Jones', 'age': 45, 'pay': 40000, 'job': 'hdw'}

names = ['name', 'age', 'pay', 'job']
values = ['Sue Jones', 45, 40000, 'hdw']

sue = dict(zip(names, values))

bob2 = {'name': {'first': 'Bob', 'last': 'Smith'},
                'age': 42,
                'job': ['software', 'writing'],
                'pay': (40000, 50000)}

db = {}
db['bob'] = bob
db['sue'] = sue

