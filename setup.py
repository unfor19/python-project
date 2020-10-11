from setuptools import setup, find_packages  # noqa: 401

with open("README.md", "r") as fh:
    readme = fh.read()

with open("version", "r") as fh:
    version = fh.read()

setup(
    author='Meir Gabay',
    author_email='unfor19@gmail.com',
    name='unfor19-python-project',
    license='MIT',
    long_description_content_type='text/markdown',
    description='Python project template',  # noqa: E501
    long_description=readme,
    version=f'{version}',
    # packages=find_packages() # must add __init__.py to each package directory
    packages=['appy', 'appy.core', 'appy.utils'],
    keywords='python project template',
    include_package_data=True,
    url='https://github.com/unfor19/python-project',
    download_url=f'https://github.com/unfor19/python-project/archive/v{version}.tar.gz',  # noqa: E501
    entry_points='''
        [console_scripts]
        appy=appy.__main__:main
    ''',
    setup_requires=[
        'setuptools>=44.1.0',
        'wheel>=0.34.2',
        'twine==3.1.1',
        'docutils>=0.16'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
    ],
)
