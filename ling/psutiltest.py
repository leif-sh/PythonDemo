#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""a common module"""
__author__ = 'ling'


import psutil


print(psutil.cpu_count())
print(psutil.cpu_count(logical=False))