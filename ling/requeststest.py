#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""a common module"""
__author__ = 'ling'


import requests


r = requests.get('https://www.douban.com/')
print(r.status_code)
print(r.text)