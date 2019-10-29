import pickle

d = dict(url='index.html', title='首页', content='首页')
ds = pickle.dumps(d)
print(ds)
dls = pickle.loads(ds)
print(dls)

# with open('dump.txt', 'wb') as f:
#     pickle.dump(d, f)

with open('dump.txt', 'rb') as f:
    dl = pickle.load(f)
print(dl)
