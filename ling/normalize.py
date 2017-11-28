#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" 
@Author:ling 
@Date: 2017/11/13 
"""
from functools import reduce


def normalize(name):
    return name[0:1].upper()+name[1:].lower()

# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(normalize, L1))
#print(L2)


def prod(list1):
    def mu(x, y):
        return x * y
    return reduce(mu, list1)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
