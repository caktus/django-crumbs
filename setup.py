import os
from setuptools import setup, find_packages

packages = find_packages()
packages.remove('sample_project')

setup(
    name='django-crumbs',
    version=__import__('crumbs').__version__,
    author='Caktus Consulting Group',
    author_email='solutions@caktusgroup.com',
    packages=find_packages(),
    include_package_data = True,
    exclude_package_data={
        '': ['*.sql', '*.pyc',],
    },
    url='http://github.com/caktus/django-crumbs/',
    license='LICENSE.txt',
    description='A pluggable Django app for adding breadcrumbs to your project. ',
    classifiers=[
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
    ],
    long_description=open('README.rst').read(),
)
