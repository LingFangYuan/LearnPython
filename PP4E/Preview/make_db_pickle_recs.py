#!/usr/bin/env python3
# -*- conding: utf-8 -*-

import pickle
from initdata import bob, sue, tom

for key, record in [('bob', bob), ('sue', sue), ('tom', tom)]:
    recfile = open(key + '.pkl', 'wb')
    pickle.dump(record, recfile)
    recfile.close()
