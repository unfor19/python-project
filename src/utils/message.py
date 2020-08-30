import os
from pathlib import Path


def greet(name):
    print(f"Hello {name}")


def script_path(file_object):
    """file_object = \\_\\_file\\_\\_"""
    abs_path = os.path.abspath(file_object)
    home_path = str(Path.home())
    relative_path = abs_path.replace(f"{home_path}", "")[1:]
    print(f"My Path: {relative_path}")


if __name__ == "__main__":
    script_path(__file__)
