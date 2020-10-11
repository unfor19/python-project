# python-project

Python project structure, relative imports, absolute imports, packages, and modules. Let's make it simpler.

## Getting Started

Executing modules from the project's root directory (top-level package)

- [main.py](./main.py)

  ```bash
  meirgabay@~/python-project (master)$ python main.py
  My Path: python-project/main.py
  Insert your name: willy
  Hello willy


  meirgabay@~/python-project (master)$ python -m appy
  My Path: python-project/appy/__main__.py
  Insert your name: willy
  Hello willy
  ```

- [appy/core/app.py](./appy/core/app.py)

  ```bash
  # Contains relative imports - `..utils.message`
  meirgabay@~/python-project (master)$ python appy/core/app.py
  Traceback (most recent call last):
    File "appy/core/app.py", line 1, in <module>
      from ..utils import message
  ImportError: attempted relative import with no known parent package


  meirgabay@~/python-project (master)$ python -m appy.core.app
  My Path: python-project/appy/core/app.py
  Insert your name: willy
  Hello willy
  ```

- [appy/utils/message.py](./appy/utils/message.py)

  ```bash
  # Doesn't contain relative imports, so no exceptions were raised
  meirgabay@~/python-project (master)$ python appy/utils/message.py
  My Path: python-project/appy/utils/message.py

  meirgabay@~/python-project (master)$ python -m appy.utils.message
  My Path: python-project/appy/utils/message.py
  ```

## Questions and Answers (Q&A)

### Project, Packages, Modules and Scripts, what are they?

- Project - a directory, also known as the top-level package, which contains packages and modules
- Package (in a project) - a directory which contains modules and/or packages (sub-directories)
- Script - a Python script (`.py`) which can be exected from the terminal
- Module - a Python script (`.py`) which can be imported with `import` and `from`

### What about Packages which are not part of a project?

- Package (built-in) - a package which is shipped with Python and can be imported with `import` and `from`
- Package (pip) - a package which is installed with [pip](https://pypi.org/project/pip/) and can be imported with `import` and `from`. Think about it, pip stands for **P**ackage **I**nstaller for **P**ython

### How do I import Packages and Modules that I've created?

- Python project's packages and modules can be imported with **relative paths** from any module which is **part of the same project**. An example is available in [appy/core/app.py](https://github.com/unfor19/python-project/blob/master/appy/core/app.py#L1)

- If you intend to import a package or a module which is **not part of the same project**, you'll have to use **absolute paths**. This can be done with [importlib](https://docs.python.org/3/library/importlib.html), see this [StackOverflow answer](https://stackoverflow.com/questions/67631/how-to-import-a-module-given-the-full-path).

### Do I need the \_\_init\_\_.py file?

- Short answer - **it depends**
- In previous versions of Python, you had to create the `__init__.py` file in each directory that you want to import as a package, they were called _regular packages_. From version 3.3+ it is not required anymore - [Implicit Namespace Packages](https://www.python.org/dev/peps/pep-0420/), packages without an `__init__.py` file are called _namespace packages_
- When creating a Python package with [setuptools](https://pypi.org/project/setuptools/), you'll need to add `__init__.py` to all of the `packages`, so the functions [find_packages](https://setuptools.readthedocs.io/en/latest/userguide/package_discovery.html?highlight=find_packages#using-find-or-find-packages) will be able to automatically import them. Read more about here in the docs - [Listing whole packages](https://docs.python.org/3/distutils/setupscript.html#listing-whole-packages)
- An alternative for adding `__init__.py` file is to manually add the names of the packages that you want to include in `setup.py`. Finally the possible solutions for packaging -

  Add `__init__.py` to each package directory, and use `find_packages()`

  ```
  packages=find_packages()
  ```

  **OR** manually declare the packages to include in [setup.py](./setup.py)
  <br>I prefer this approach, it helps keeping the project clean from `__init__.py`, and the package management is solely managed in `setup.py`

  ```
  packages=['appy', 'appy.core', 'appy.utils']
  ```

### Why do relative imports raise a problem in pylint?

The error - `Attempted relative import beyond top-level packagepylint(relative-beyond-top-level)`

- Short answer - **I don't know**
- All I can say is that it doesn't happen with [flake8](https://flake8.pycqa.org/en/latest/)

### Is it possible to invoke a function from the terminal?

- Short answer - **it depends**

- Trying to invoke a function from the terminal, such as `appy.core.app.main()`, will raise the ModuleNotFound exception. A package must be imported **before** invoking one of its functions.

  ```bash
  meirgabay@~/python-project (master)$ python -m appy.core.app.main
  /Users/meirgabay/.pyenv/versions/3.8.2/Python.framework/Versions/3.8/bin/python: Error while finding module specification for 'appy.core.app.main' (ModuleNotFoundError: __path__ attribute not found on 'appy.core.app' while trying to find 'appy.core.app.main')
  ```

- Since you can't invoke `main()` directly from the terminal, calling it from the `if __main__` block enables executing it from the terminal. It's possible to pass arguments, but it's a bit ugly, [read the docs](https://docs.python.org/3/using/cmdline.html) to learn how. The following example attempts to execute the module `appy.core.app`, which in turn call its `if __main__` block

  ```bash
  meirgabay@~/python-project (master)$ python -m appy.core.app
  My Path: python-project/appy/core/app.py
  Insert your name: willy
  Hello willy
  ```

- If the `PWD` is a subdirectory of the project, such as `python-project/appy`, an attempt to execute a module which contains relative imports, will raise the exception below. Remember, your `PWD` should always be the project's root directory, in this case it's `python-project`.

  ```bash
  # PWD is `appy`
  meirgabay@~/python-project/appy (master)$ python -m core.app

  Traceback (most recent call last):
    File "/Users/meirgabay/.pyenv/versions/3.8.2/Python.framework/Versions/3.8/lib/python3.8/runpy.py", line 193, in _run_module_as_main
      return _run_code(code, main_globals, None,
    File "/Users/meirgabay/.pyenv/versions/3.8.2/Python.framework/Versions/3.8/lib/python3.8/runpy.py", line 86, in _run_code
      exec(code, run_globals)
    File "/Users/meirgabay/python-project/appy/core/app.py", line 1, in <module>
      from ..utils import message
  ValueError: attempted relative import beyond top-level package
  ```

- It doesn't happen when invoking `message`, since `message` doesn't use relative imports

  ```bash
  meirgabay@~/python-project/appy (master)$ python utils/message.py
  My Path: python-project/appy/utils/message.py


  meirgabay@~/python-project/appy (master)$ python -m utils.message
  My Path: python-project/appy/utils/message.py
  ```

- Invoking a function from the terminal is also possible by using the `-c` flag. Surprise, it's possible to pass arguments in a more intuitive way, for example `app.main(my_arg1, my_arg2)`
  ```bash
  meirgabay@~/python-project (master)$ python -c "import appy.core.app as app; app.main()"
  Insert your name: willy
  Hello willy
  ```

### What are the available command-line flags in Python?

- Read the docs - [using cmdline](https://docs.python.org/3/using/cmdline.html)
- In this tutorial, we used both `-c` and `-m` flags

### Why is it possible to execute `python -m appy`?

The [appy/\_\_main\_\_.py](./appy/__main__.py) file acts like the `if __main__` code snippet, but on packages. This enables the `appy` package to be executed with `python -m` or with [runpy](https://docs.python.org/3/library/runpy.html)

```bash
meirgabay@~/python-project (master)$ python -m appy
My Path: python-project/appy/__main__.py
Insert your name: willy
Hello willy
```

### What's `runpy` and why do you use it in `main.py`?

The `runpy` package provides the ability to run modules from a module (Python script).

[main.py](./main.py)

```python
import runpy


def main():
    # import a package, and pass all current global variables to it
    appy_package = runpy.run_module(mod_name="appy", init_globals=globals())

    # import the function script_path() from the submodule message, and execute it
    appy_package['message'].script_path(__file__)

    # execute the function main(), which is located in appy/__main__.py
    appy_package['main']()


if __name__ == "__main__":
    main()
```

### What's `globals()`?

The official definition from the [docs](https://docs.python.org/3/library/functions.html#globals)

> Return a dictionary representing the current global symbol table. This is always the dictionary of the current module (inside a function or method, this is the module where it is defined, not the module from which it is called).

<details><summary>Example - Expand/Collapse

</summary>

```bash
meirgabay@~/python-project (master)$ python
Python 3.8.2 (default, Jun 30 2020, 19:04:41)
[Clang 11.0.3 (clang-1103.0.32.59)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> globals()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>}
```

</details>

### Why do you have a weird path with `pyenv` when you run Python?

In some of the examples you might have seen that my Python binary is located in

```
/Users/meirgabay/.pyenv/versions/3.8.2/Python.framework/Versions/3.8/bin/python
```

This is because I'm using [pyenv](https://github.com/pyenv/pyenv), the official definition from the docs

> pyenv lets you easily **switch between multiple versions of Python**. It's simple, unobtrusive, and follows the UNIX tradition of single-purpose tools that do one thing well.

- pyenv great for checking backwards compatibility

- Switching to a different version

  1. Install relevant version - `pyenv install 3.7.7`
  2. Run `export PYENV_VERSION=3.7.7`

- For a day to day use

  1. Install relevant version - `pyenv install 3.8.2`
  2. Add `export PYENV_VERSION=3.8.2` to your terminal's `rc` or `_profile` (`$HOME/.bashrc`, `$HOME/.bash_profile`, `$HOME/.zshrc`)

<details><summary>Examples - Expand/Collapse

</summary>

```bash
meirgabay@~/python-project (master)$ export PYENV_VERSION=
meirgabay@~/python-project (master)$ pyenv versions
* system (set by /Users/meirgabay/.pyenv/version) # default OS Python
  3.7.7
  3.8.2
meirgabay@~/python-project (master)$ python --version
Python 2.7.16

# switching to a different version
meirgabay@~/python-project (master)$ export PYENV_VERSION=3.7.7
meirgabay@~/python-project (master)$ python --version
Python 3.7.7

# day to day use
meirgabay@~/python-project (master)$ source ~/.bash_profile
meirgabay@~/python-project (master)$ python --version
Python 3.8.2
```

</details>

### Is there a good framework for creating a Python CLI?

- Short answer - **yes! more than a few!**
- The [Click Framework](https://click.palletsprojects.com/en/7.x/) is amazing! I used it in [githubsecrets](https://github.com/unfor19/githubsecrets) and [frigga](https://github.com/unfor19/frigga)
  <br>_NOTE_: you'll discover that I have `__init__.py` files in my projects, that's a nasty old habit, I promise I will drop them, I promise
- Read more about the available Python CLI frameworks in this great blog post - [Building Beautiful Command Line Interfaces with Python](https://codeburst.io/building-beautiful-command-line-interfaces-with-python-26c7e1bb54df)

### Where can I find a well-structured Python project?

- [sampleproject](https://github.com/pypa/sampleproject) - the official Python sample project
- [Django](https://github.com/django/django) - a complex Python project
- [requests](https://github.com/psf/requests) - a non-complex Python project

## Final words

I hope that this blog post helped you in understanding how to create a well-structured Python project, and if it did, then Heart, Clap, Star and share!

## Authors

Created and maintained by [Meir Gabay](https://github.com/unfor19)
