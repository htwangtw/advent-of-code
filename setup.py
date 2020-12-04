#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages
setup(
    author="Hao-Ting Wang",
    author_email='htwangtw@gmail.com',
    python_requires='>=3.5',
    description="aoc",
    entry_points={
        'console_scripts': [
            'pyretroicor=pyretroicor.cli:main',
        ],
    },
    name='aoc',
    packages=find_packages(),
    version='0.0.3',
)