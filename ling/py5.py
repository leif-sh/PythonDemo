#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import  Iterable


# x = isinstance('abc', Iterable)
# print(x)
#
# y = isinstance([1, 2, 3], Iterable)
# print(y)
#
# z = isinstance(123, Iterable)
# print(z)

for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)
