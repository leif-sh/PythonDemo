#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""a common module"""
__author__ = 'ling'

# try:
#     f = open('d:/a.txt', 'r')
#     print(f.read())
# finally:
#     if f:
#         f.close()

# with open('d:\\a.txt', 'r') as f:
#     for line in f.readlines():
#         print(line.strip())

# 读取二进制文件
# with open('test.jpg', 'rb') as f:
#     print(f.read())

# with open('d:/a.txt', 'r', encoding='gbk', errors='ignore') as f:
#     print(f.read())

with open('d:/a.txt', 'r') as f:
    str = f.read()
    with open('d:/a.txt', 'w') as f1:
        f1.write(str+'Hello world!')

