import os
from setuptools import setup, find_packages

setup(
    name='django-crumbs',
    version='0.0.0',
    author='Caktus Consulting Group',
    author_email='solutions@caktusgroup.com',
    packages=find_packages(),
    install_requires = ['Django >= 1.1,==dev',],
    include_package_data = True,
    exclude_package_data={
        '': ['*.sql', '*.pyc',],
    },
    url='http://code.google.com/p/django-crumbs/',
    license='LICENSE.txt',
    description='A pluggable Django app for adding breadcrumbs to your project. ',
    long_description=open('README.txt').read(),
)
