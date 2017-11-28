#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""a common module"""
__author__ = 'ling'


import os
# print(os.name)
# print(os.environ)
# print(os.environ.get('classpath'))
# print(os.path.abspath('.'))
# print(os.path.join('d:\\user', 'testdir2'))
# print(os.path.split('d:/users/micharl/123'))

import shutil

# shutil.copyfile('d:\\a.txt','d:\\b.txt')

print([x for x in os.listdir('.') if os.path.isfile(x)])
os.chdir('d:')
print([x for x in os.listdir('D:\\')])
print(os.path.isdir('D:\\$RECYCLE.BIN'))