import pickle


data = {'a', 'b'}
with open('test.txt', 'wb', encoding='utf-8') as f:
    pickle.dump(data, f)
