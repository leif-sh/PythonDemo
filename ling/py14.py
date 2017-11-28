#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" 
@Author:ling 
@Date: 2017/11/15 
"""
import functools


# def int2(x, base=2):
#     return int(x, base)
#
# print(int2('1000'))

int2 = functools.partial(int, base=2)
print(int2('1000'))
