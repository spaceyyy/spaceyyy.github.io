#!python3
# setup.py - File that is necessary for a distribution package.
#            This is going to be for the vsearch.py file


from setuptools import setup

setup(
    name='vsearch',
    version='1.0',
    description='The Head First Python Search Tools',
    author='HF Python 2e',
    author_email='hfpy2e@gmail.com',
    py_modules=['vsearch'],
)