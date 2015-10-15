from setuptools import setup, find_packages

from codecs import open
from os import path
import sys

BASE_DIR = path.abspath(path.dirname(__file__))

with open(path.join(BASE_DIR, 'README.md'), encoding='utf-8') as f:
	long_description = f.read()

setup(
	name='pycodechef',
	version='0.0.1.dev1',
	description='Codechef Python Package',
	license='MIT',
	classifiers=[
		# How mature is this project? Common values are
		#   3 - Alpha
		#   4 - Beta
		#   5 - Production/Stablegit
		'Development Status :: 3 - Alpha',
		'Intended Audience :: Developers',
		'Topic :: Software Development :: Build Tools',
		'License :: OSI Approved :: MIT License',

		# Specify the Python versions you support here. In particular, ensure
		# that you indicate whether you support Python 2, Python 3 or both.
		'Programming Language :: Python :: 2',
		'Programming Language :: Python :: 2.6',
		'Programming Language :: Python :: 2.7',
	],
	long_description=long_description,
	author='DESHRAJ',
	author_email='deshrajdry@gmail.com',
	url='https://github.com/deshraj/pycodechef',
	keywords = "codechef programming challenges competitive topcoder spoj leetcode hackerrank hackerearth codeforces tool cli",
	packages=['codechef'],
	install_requires=[
		"click>=5.0",
		"requests==2.7.0"
	] + (["colorama==0.3.3"] if "win" in sys.platform else []),
	entry_points = {
		'console_scripts': [
			'codechef = codechef.cli:main'
		],
	}
	)