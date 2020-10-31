from os import getcwd, path
from setuptools import setup

with open("README.md", "r") as fh:
    readme = fh.read()

with open("version", "r") as fh:
    version = fh.read()

# with open(path.join(getcwd(), 'appy', '__init__.py'), "w") as fh:
#     fh.write(f"__version__ = '{version}'")
version = '0.0.1'

setup(
    version=f'{version}',
    download_url=f'https://github.com/unfor19/python-project/archive/v{version}.tar.gz',  # noqa: E501
)
