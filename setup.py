import pkg_resources
import os
from setuptools import setup, find_packages


def dependencies():
    file_ = pkg_resources.resource_filename(__name__, os.path.join('requirements', 'default.txt'))
    with open(file_, 'r') as f:
        return f.read().splitlines()


setup(name='cami-amber',
      version='1.0',
      description='AMBER: Assessment of Metagenome BinnERs',
      url='https://github.com/CAMI-challenge/AMBER',
      author='CAMI',
      author_email='fernando.meyer@gmail.com',
      license='Apache 2.0',
      packages=find_packages(),
      install_requires=dependencies())
