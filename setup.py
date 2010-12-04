from setuptools import setup, find_packages

setup(
    name='django-crumbs',
    version=__import__('crumbs').__version__,
    author='Caktus Consulting Group',
    author_email='solutions@caktusgroup.com',
    include_package_data=True,
    packages=find_packages(exclude=['sample_project']),
    exclude_package_data={'': ['*.sql', '*.pyc']},
    url='http://github.com/caktus/django-crumbs/',
    license='BSD',
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
    zip_safe=False,
)

