
from setuptools import setup
import sys
import os

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
    long_description = open('README.md').read()

install_requires = [
    'numpy',
    'nltk',
    'jellyfish',
    'pycountry',
    'newspaper;python_version<"3.0"',
    'newspaper3k;python_version>="3.0"'
]

setup(name='geograpy',
      version='0.3.7',
      description='Extract countries, regions and cities from a URL or text',
      long_description=long_description,
      url='https://github.com/ushahidi/geograpy',
      download_url ='https://github.com/ushahidi/geograpy/tarball/0.3.4',
      author='Jonathon Morgan',
      author_email='jonathon@ushahidi.com',
      license='MIT',
      packages=['geograpy'],
      install_requires=install_requires,
      scripts=['geograpy/bin/geograpy-nltk'],
      package_data = {'geograpy': ['data/*.csv'],},
      zip_safe=False)
