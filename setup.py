from setuptools import setup, find_packages

setup(name='NathanJamesToolbox',
      version='0.0.1',
      description='This package has components used for NJ specific work.',
      author='Paulo Fajardo',
      author_email='paulo.fajardo@nathanjames.com',
      packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests", '*.csv']),
      license='LICENSE.txt')
