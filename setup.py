# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='sphinx_distutils',
    author='Kevin Schlosser',
    author_email='kevin.g.schlosser@gmail.com',
    version='0.1.0',
    zip_safe=False,
    url='https://github.com/kdschlosser/sphinx-distutils-extension',
    description='a more full featured distutils/setuptools build command',
    packages=find_packages('sphinx_distutils'),
    package_dir=dict(
        sphinx_distutils='sphinx_distutils',
    )
)
