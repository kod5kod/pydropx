#!/usr/bin/env python

from setuptools import setup, find_packages
version = 'v0.4 Beta'
setup(
	name = 'pydropx',
	version = version,
	description = 'A simple dropbox wrapper for uploading files and folders',
	author = 'Datuman',
	url = 'https://github.com/kod5kod',
	include_package_data = True,
	packages = find_packages(),
	install_requires = [
		]
)





