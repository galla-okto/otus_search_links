import os
from setuptools import setup, find_packages

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='search_links',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='GNU General Public License v3.0',
    description='search links',
    # long_description=README,
    url='https://github.com/galla-okto/otus_search_links',
    author='Anna',
    author_email='galla.okto1@gmail.com',
    keywords = ['search_links'],
    # classifiers = [],
    entry_points={
        'console_scripts': [
            'find_links = search.main:main',
        ]
    },
)