#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""a common module"""
__author__ = 'ling'


import pickle
# d = dict(name='Bob', age=20, score=88)
# pickle.dumps(d)

# f = open('D:\\a.txt', 'wb')
# pickle.dump(d, f)
# f.close()

# f = open('D:\\a.txt', 'rb')
# d = pickle.load(f)
# f.close()
# print(d)

import json
# d = dict(name='Bob', age=20, score=88)
# f = open('D:\\a.txt', 'w')
# json.dump(d, f)
# f.close()

# with open('D:\\a.txt', 'r') as f:
#     d = json.load(f)
# print(d)


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Bob', 20, 68)

def stu2json(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }

print(json.dumps(s, default=lambda x:x.__dict__))