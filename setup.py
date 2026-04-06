#!/usr/bin/env python
# This file is part of Viper - https://github.com/viper-framework/viper
# See the file 'LICENSE' for copying permission.

from setuptools import setup

setup(
    name='pefile-tests',
    version='0.2',
    author='Viper authors, Philippe Ombredanne and others',
    description='Test suite for pefile',
    url='http://viper.li',
    license='BSD-3-Clause and MIT',
    install_requires=['pefile'],
    extras_require={'testing': ['pytest', 'pytest-xdist']},
)
