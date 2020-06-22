#!/usr/bin/env python

from setuptools import setup, find_packages
import sys

if not (sys.version_info.major == 3 and sys.version_info.minor >= 7):
    print("[!] SQLiFinder requires Python 3.7 or higher!")
    print(
        "[*] You are using Python {}.{}.".format(
            sys.version_info.major, sys.version_info.minor
        )
    )
    sys.exit(1)

with open("requirements.txt") as fp:
    required = [line.strip() for line in fp if line.strip() != ""]

setup(
   name='sqlifinder',
   version='1.0',
   description='Program to scrape entries from Google using a dork and test each of those entries for basic SQL injection vulnerabilities',
   author='Roberto Reigada Rodríguez',
   url='https://github.com/roberreigada/sqlifinder',
   license='apache 2.0',
   author_email='roberreigada@gmail.com',
   packages=find_packages(),
   install_requires=required,
   python_requires='>=3.7'
)
#long_description=open('README.md').read(),
