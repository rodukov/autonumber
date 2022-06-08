from setuptools import setup, find_packages
import codecs
import os

VERSION = '1.0.0'
DESCRIPTION = ' Useful utility that allows you to generate cell phone numbers of all countries of the world'

# Setting up
setup(
    name="autonumber",
    version=VERSION,
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['list', 'awesome', 'generator', 'phonenumber', 'autonumber'],
)