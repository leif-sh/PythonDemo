#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math


# def fact(n):
#     if n == 1:
#         return 1
#     print('%d * fact(%d - 1)', n, n)
#     return n * fact(n - 1)
# print(fact(5))

def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)
move(2, 'A', 'B', 'C')
