# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='python bowling kata',
    version='0.1.0',
    description='Uncle Bob\'s Bowling Kata in Python',
    long_description=readme,
    author='Randall Loffelmacher',
    author_email='randy@loffelmacher.com',
    url='https://github.com/loffelmacher/py-bowling',
    license=license,
    packages=find_packages(exclude=('tests'))
)

