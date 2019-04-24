#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pickle
from initdata import db

dbfile = open("people-pickle", 'wb') # 二进制写模式打开文件
pickle.dump(db, dbfile)
dbfile.close()
