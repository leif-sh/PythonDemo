#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""a common module"""
__author__ = 'ling'


from datetime import datetime

# now = datetime.now()
# print(now)
# print(type(now))

# dt = datetime(2015, 4, 19)
# print(dt.timestamp())

cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)