#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" 
@Author:ling 
@Date: 2017/11/13 
"""


def triangles(maxline):
    a, li = 0, [1]
    while a < maxline:
        yield li
        li = [1] + [li[x] + li[x+1] for x in range(a)] + [1]
        a += 1

n = 0
for t in triangles(10):
    print(t)
    n += 1
    if n == 10:
        break
