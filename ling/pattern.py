#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""a common module"""
__author__ = 'ling'


import re
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')

print(re.match(r'^\d{3}\-\d{3,8}$', '010-12345'))

# test = '用户输入的字符串'
# if re.match(r'正则表达式', test):
#     print('ok')
# else:
#     print('failed')

# print('a b      c'.split(' '))
# print(re.split(r'\s+', 'a b   c'))

print(m.group(0))
print(m.group(1))
print(m.group(2))