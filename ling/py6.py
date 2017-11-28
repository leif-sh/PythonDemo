#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" 
@author:ling 
@file: py6.py 
@time: 2017/11/08 
"""


# x = [x * x for x in range(1, 11)]
# print(x)
#
# x = [x * x for x in range(1, 11) if x % 2 == 0]
# print(x)
#
# x = [m + n for m in 'ABC' for n in 'XYZ']
# print(x)

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x.lower() for x in L1 if isinstance(x, str)]
print(L2)

g = (x * x for x in range(10))
for n in g:
    print(n)
