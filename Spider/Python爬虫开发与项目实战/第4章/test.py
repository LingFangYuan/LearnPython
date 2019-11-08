import os

path = 'F:\BaiduNetdiskDownload\豆瓣高分电子书合集'.replace('\\', '/')

with open('书目.txt', 'w', encoding='utf-8') as f:
    for fname in os.listdir(path):
        fname = fname.rstrip('.epub')
        print(fname)
        f.write(fname + '\n')
