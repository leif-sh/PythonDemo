#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" 
@Author:ling 
@Date: 2017/11/14 
"""


def is_palindrome(n):
    tem = ''
    for num in str(n):
        tem = num + tem
    return int(tem) == n

output = filter(is_palindrome, range(1, 1000))
print(list(output))
