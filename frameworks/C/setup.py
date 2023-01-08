#!/usr/bin/env python3

from setuptools import setup, Extension


setup(
    name="fputs",
    version="1.0.0",
    description="Python interface for the fputs C library function",
    author="<your name>",
    author_email="your_email@gmail.com",
    ext_modules=[Extension("fputs", ["fputsmodule.c"])]
)
