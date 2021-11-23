from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='canvas_roof_count',
    version='1.0',
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.txt')).read(),
    py_modules=['canvas_roof', ],
    install_requires=[
        'autopep8=1.5.7',
        'canvas-roof-count=1.0',
        'numpy=1.21.2',
        'pycodestyle=2.7.0',
        'toml=0.10.2',
    ]
)
