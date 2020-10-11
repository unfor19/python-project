import os
from pathlib import Path
from requests import request


def get_fact():
    req = request('get', 'https://catfact.ninja/fact')
    try:
        return req.json()['fact']
    except Exception as e:
        print(e)
        exit()


def greet(name: str):
    fact = get_fact()
    msg = f"\nHello {name.title()}, here's the cat fact of the day:\n{fact}\n"
    print(msg)


def script_path(file_object):
    """file_object = \\_\\_file\\_\\_"""
    abs_path = os.path.abspath(file_object)
    home_path = str(Path.home())
    relative_path = abs_path.replace(f"{home_path}", "")[1:]
    print(f"My Path: {relative_path}")


if __name__ == "__main__":
    script_path(__file__)
