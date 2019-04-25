#!/usr/bin/env python3
# -*- conding: utf-8 -*-

import shelve

db = shelve.open('people-shelve')
sue = db['sue']
sue['pay'] *= 1.5
db['sue'] = sue
db['ling'] = {}
db.close()
