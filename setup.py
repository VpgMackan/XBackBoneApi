# setup.py
from setuptools import setup, find_packages

setup(
    name="xbackboneapi",
    version="0.21",
    packages=find_packages(),
    install_requires=[
        "requests",
        "lxml",
        "typing",
    ],
)
