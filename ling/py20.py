#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""a common module"""
__author__ = 'ling'


# class Student(object):
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return 'Student object (name: %s)' % self.name
#
# print(Student('Michael'))

# class Fib(object):
#     def __init__(self):
#         self.a, self.b = 0, 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.a, self.b = self.b, self.a + self.b
#         if self.a > 100000:
#             raise StopIteration()
#         return self.a
# for n in Fib():
#     print(n)

# class Fib(object):
#     def __getitem__(self, item):
#         a, b = 1, 1
#         for x in range(item):
#             a, b = b, a + b
#         return a
# f = Fib()
# print(f[0])


class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s' % self.name)
s = Student('Michael')
s()