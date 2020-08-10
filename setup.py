#! /usr/bin/env python3

import setuptools

with open('README.md') as fh:
    long_description = fh.read()

setuptools.setup(
    name='ping',
    version='0.1',
    #scripts=['ping'],
    author='Fernando Abreu',
    author_github='https://github.com/nandoabreu',
    description='Python ping package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/nandoabreu/python-ping',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)

