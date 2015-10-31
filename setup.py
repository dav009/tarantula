#!/usr/bin/env python -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name='tarantula',
    version='0.1',
    packages=['tarantula',],
    description='scraper + parser',
    long_description='Scraper + parser for dumping data from gov websites',
    license="",
    install_requires = ["requests>=2.6", "lxml>=3.3.3", "pyexcel_xls", "cssselect>=0.9.1"]
)