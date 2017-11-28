#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" 
@Author:ling 
@Date: 2017/11/13 
"""
from functools import reduce


# def str2float(string):
#     def la(s):
#         return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, "7": 7, '8': 8, '9': 9}[s]
#     tem = string.split('.')
#
#     def fun1(x, y):
#         return x * 10 + y
#
#     n = 10
#
#     def fun2(x, y):
#         nonlocal n
#         temq = x + y / n
#         n *= 10
#         return temq
#
#     return reduce(fun1, map(la, tem[0])) + reduce(fun2, map(la, tem[1])) * 0.1
# print('str2float(\'123.456\') =', str2float('123.456'))

CHAR_TO_FLOAT = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, "7": 7, '8': 8, '9': 9, '.': -1}


def str2float(s):
    nums = map(lambda ch: CHAR_TO_FLOAT[ch], s)
    point = 0

    def to_float(f, n):
        nonlocal point
        if n == -1:
            point = 1
            return f
        if point == 0:
            return f * 10 + n
        else:
            point *= 10
            return f + n / point
    return reduce(to_float, nums, 0.0)
print(str2float('123.456'))
