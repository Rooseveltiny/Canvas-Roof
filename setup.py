from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='canvas_roof_count',
    version='1.0',
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.txt')).read(),
    py_modules=['canvas_roof', ],
    install_requires=[
        'autopep8',
        'numpy',
        'pycodestyle',
        'toml',
    ]
)
