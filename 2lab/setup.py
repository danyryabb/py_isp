from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='MyParser',
    version='1.0',
    long_description=open(join(dirname(__file__), 'README.txt')).read(),
    packages=find_packages(include=['MyParser', 'MyParser.*']),
    entry_points={
        'console_scripts':
            ['MyParser = MyParser.main:start_app'],
        },
    install_requires=[
        'coverage==5.5',
        'entrypoints==0.3',
        'py==1.10.0',
        'pytest==6.2.3',
        'pytest-cov==2.11.1',
        'PyYAML==5.4.1',
        'simplejson==3.16.0',
        'toml==0.10.2',
        'virtualenv==20.0.17',
    ]
)