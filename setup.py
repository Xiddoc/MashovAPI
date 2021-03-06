#!/usr/bin/env python
# coding: utf-8

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="MashovAPI",
    version="1.1.7",
    author="Xiddoc",
    author_email="sajihajyehia@gmail.com",
    description="The Unofficial Mashov API, giving you access to all existing features.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Xiddoc/MashovAPI",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)