#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name="andrawpick",
      py_modules=['andrawpick'],
      version="0.1",
      description="A simple script to pick Android drawables from a folder and put them into your project.",
      license="MIT",
      author="Nephila",
      author_email="stagi.andrea@gmail.com",
      url="",
      keywords= "android drawable utils",

      entry_points = {
        'console_scripts': [
            'andrawpick = andrawpick:main',
        ],
      },
      zip_safe = True)