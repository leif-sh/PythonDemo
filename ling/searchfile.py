#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""a common module"""
__author__ = 'ling'
import os


def searchfile(str, dir):
    if os.access(dir, os.R_OK):
        for x in os.listdir(dir):
            y = os.path.join(dir, x)
            if os.path.isdir(y):
                if x.startswith('$'):
                    pass
                else:
                    searchfile(str, y)
            if os.path.isfile(y):
                if x.__contains__(str):
                    print(os.path.abspath(y))


searchfile('py', 'D:\\WorkspaceForAllIDE')
