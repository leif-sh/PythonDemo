#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""a common module"""
__author__ = 'ling'
from enum import Enum


Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
print(Month.Jan)

for name, member in Month.__members__.items():
    print(name, '==>', member, ',', member.value)