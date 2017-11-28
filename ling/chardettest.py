#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""a common module"""
__author__ = 'ling'


import chardet

print(chardet.detect(b'Hello, world'))

data = '离离原上草，一岁一枯荣'.encode('gbk')
print(chardet.detect(data))