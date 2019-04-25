#!/usr/bin/env python3
# -*- conding: utf-8 -*-

import pickle, glob

for filename in glob.glob('*.pkl'):
    recfile = open(filename, 'rb')
    record = pickle.load(recfile)
    print(filename, '=>\n', record)
    recfile.close()

suefile = open('sue.pkl', 'rb')
print(pickle.load(suefile)['name'])
