#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""a common module"""
__author__ = 'ling'


class Animal(object):
    def run(self):
        print('Animal is runing...')


class Dog(Animal):
    def __len__(self):
        return 100
    pass


class Cat(Animal):
    pass

dog = Dog()
print(len(dog))