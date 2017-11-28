#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""a common module"""
__author__ = 'ling'


import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()

cursor.execute('CREATE TABLE user (id varchar(20) PRIMARY KEY , name varchar(20))')
cursor.execute('INSERT INTO user (id, name) VALUES (\'1\', \'Michael\')')

print(cursor.rowcount)
cursor.close()
conn.commit()
conn.close()