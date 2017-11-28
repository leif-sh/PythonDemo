#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""a common module"""
__author__ = 'ling'


class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_name(self):
        return self.__name
bart = Student('Bart Simpson', 98)
print(bart.get_name())
bart._Student__name = 'New Name'

print(bart.get_name())
