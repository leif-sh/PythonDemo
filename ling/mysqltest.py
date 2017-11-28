#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""a common module"""
__author__ = 'ling'


import mysql.connector

conn = mysql.connector.connect(user='root', password='1234', database='test')
cursor = conn.cursor()

cursor.execute('create  table user (id VARCHAR(20) PRIMARY KEY , name VARCHAR (20))')
cursor.execute('insert into user (id, name) VALUE (%s,%s)', ['1','Michael'])
print(cursor.rowcount)

conn.commit()
cursor.close()

cursor = conn.cursor()
cursor.execute('select * from user WHERE id = %s', ('1',))
values = cursor.fetchall()
print(values)
cursor.close()
conn.close