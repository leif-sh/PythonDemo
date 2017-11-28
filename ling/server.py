#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""a common module"""
__author__ = 'ling'


from wsgiref.simple_server import make_server
from ling.hello import application

httpd = make_server('', 8000, application)
print('Serving Http on port 8000...')
httpd.serve_forever()