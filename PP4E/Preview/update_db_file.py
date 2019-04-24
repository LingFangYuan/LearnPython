#!/usr/bin/env python3
# -*- conding: utf-8 -*-

from make_db_file import loadDbase, storeDbase

db = loadDbase()
db['sue']['pay'] *= 1.10
db['tom']['name'] = 'Tom Tom'
storeDbase(db)
