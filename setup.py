#!/usr/bin/env python
#encoding:utf-8
'''
@author: yangmv
@file: setup.py
@time: 2018-12-31 16:47
'''
from distutils.core import setup

setup(
    name='opssdk',
    version='0.0.2',
    packages=['websdk'],
    url='https://github.com/yangmv/ops_sdk/',
    license='',
    install_requires=['PyJWT','redis===2.10.6'],
    author='yangmv',
    author_email='yangmv@126.com',
    description='SDK of the operation and maintenance script'
)