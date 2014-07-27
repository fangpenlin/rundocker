from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages

setup(
    name='rundocker',
    version='1.0.0',
    packages=find_packages(),
    entry_points="""\
    [console_scripts]
    rundocker = rundocker.__main__:main
    """,
)
