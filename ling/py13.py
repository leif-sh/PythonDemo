#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" 
@Author:ling 
@Date: 2017/11/14 
"""
import functools


# def now():
#     print('2015-3-25')
# f = now
# print(f.__name__)


# def log(func):
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         func(*args, **kw)
#         return None
#     return wrapper
#
#
# @log
# def now():
#     print('2015-3-25')
# now()

# def log(text):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kw):
#             print('%s %s():' % (text, func.__name__))
#             return func(*args, **kw)
#         return wrapper
#     return decorator
#
#
# @log('execute')
# def now():
#     print('1111111111')
# now()
# print(now.__name__)

# def log(func):
#     def wrapper(*args, **kw):
#         print('Begin call')
#         func(*args, **kw)
#         print('End call')
#         return None
#     return wrapper
#
#
# @log
# def now():
#     print('1111111111')
# now()

# @log
# def now():
#     print('2015-3-25')
# now()

def log(text='execute'):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log()
def now():
    print('1111111111')
now()
