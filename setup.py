# setup.py
from setuptools import setup, find_packages

setup(
    name="xbackboneapi",
    version="0.2",
    packages=find_packages(),
    install_requires=[
        "requests",
        "lxml",
        "typing",
    ],
)
