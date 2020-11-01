from os import getcwd, path
from setuptools import setup, sic

with open("README.md", "r") as fh:
    readme = fh.read()

with open("version", "r") as fh:
    version = fh.read()

with open(path.join(getcwd(), 'src', 'appy', '__init__.py'), "w") as fh:
    fh.write(f"__version__ = '{version}'\n")

setup(
    version=sic(version),
    download_url=f'https://github.com/unfor19/python-project/archive/{version}.tar.gz',  # noqa: E501
)
