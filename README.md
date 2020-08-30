# python-project

Python project structure, relative imports, absolute imports, packages, and modules. Let's make it simpler.

## Getting Started

Executing modules from the project's root directory (top-level package)

- `main.py`

  ```bash
  meirgabay@~/python-project (master)$ python main.py
  My Path: python-project/main.py
  Insert your name: willy
  Hello willy


  meirgabay@~/python-project (master)$ python -m main
  My Path: python-project/main.py
  Insert your name: willy
  Hello willy
  ```

- `app.py`

  ```bash
  # Contains relative imports - `..utils.message`
  meirgabay@~/python-project (master)$ python src/app/app.py
  Traceback (most recent call last):
    File "src/app/app.py", line 1, in <module>
      from ..utils import message
  ImportError: attempted relative import with no known parent package


  meirgabay@~/python-project (master)$ python -m src.app.app
  My Path: python-project/src/app/app.py
  Insert your name: willy
  Hello willy
  ```

- `message.py`

  ```bash
  # Doesn't contain relative imports, so no exceptions were raised
  meirgabay@~/python-project (master)$ python src/utils/message.py
  My Path: python-project/src/utils/message.py


  meirgabay@~/python-project (master)$ python -m src.utils.message
  My Path: python-project/src/utils/message.py
  ```

## Questions and Answers (Q&A)

### Project, Packages and Modules, what are they?

- Project - a directory, also known as the top-level package, which contains packages and modules
- Package (in a project) - a directory which contains modules and/or packages (sub-directories)
- Module - a Python script (`.py`) which can be exected from the terminal, or imported with `import` and `from`

### What about Packages which are not part of a project?

- Package (built-in) - a package which is shipped with Python and can be imported with `import` and `from`
- Package (pip) - a package which is installed with [pip](https://pypi.org/project/pip/) and can be imported with `import` and `from`. Think about it, pip stands for **P**ackage **I**nstaller for **P**ython

### How do I import Packages and Modules that I've created?

- Python project's packages and modules can be imported with **relative paths** from any module which is **part of the same project**. An example is available in [src/app/app.py](https://github.com/unfor19/python-project/blob/master/src/app/app.py#L1)

- If you intend to import a package or a module which is **not part of the same project**, you'll have to use **absolute paths**. This can be done with [importlib](https://docs.python.org/3/library/importlib.html), see this [StackOverflow answer](https://stackoverflow.com/questions/67631/how-to-import-a-module-given-the-full-path).

### Do I need the \_\_init\_\_.py file?

- Short answer - **no**
- In previous versions of Python, you had to create the `__init__.py` file in each directory that you want to import as a package, they were called _regular packages_. From version 3.3+ it is not required anymore - [Implicit Namespace Packages](https://www.python.org/dev/peps/pep-0420/), packages without an `__init__.py` file are called _namespace packages_.

### Why do relative imports raise a problem in pylint?

- Short answer - **I don't know**
- All I can say is that it doesn't happen with [flake8](https://flake8.pycqa.org/en/latest/)

`Attempted relative import beyond top-level packagepylint(relative-beyond-top-level)`

### Is it possible to invoke a function from the terminal?

- Short answer - **it depends**

- Trying to invoke a function from the terminal, such as `src.app.app.main()`, will raise the ModuleNotFound exception. A package must be imported **before** invoking one of its functions.

  ```bash
  meirgabay@~/python-project (master)$ python -m src.app.app.main
  /Users/meirgabay/.pyenv/versions/3.8.2/Python.framework/Versions/3.8/bin/python: Error while finding module specification for 'src.app.app.main' (ModuleNotFoundError: __path__ attribute not found on 'src.app.app' while trying to find 'src.app.app.main')
  ```

- Since you can't invoke `main()` directly from the terminal, calling it from the `if __main__` block enables executing it from the terminal. It's possible to pass arguments, but it's a bit ugly, [read the docs](https://docs.python.org/3/using/cmdline.html) to learn how. The following example attempts to execute the module `src.app.app`, which in turn call its `if __main__` block

  ```bash
  meirgabay@~/python-project (master)$ python -m src.app.app
  My Path: python-project/src/app/app.py
  Insert your name: willy
  Hello willy
  ```

- Executing a module which contains relative imports, while the `PWD` is a subdirectory of the project, such as `python-project/src`, will raise the exception below. Remember, your `PWD` should always be the project's root directory, in this case it's `python-project`.

  ```bash
  # We're in `src`
  meirgabay@~/python-project/src (master)$ python -m app.app

  Traceback (most recent call last):
    File "/Users/meirgabay/.pyenv/versions/3.8.2/Python.framework/Versions/3.8/lib/python3.8/runpy.py", line 193, in _run_module_as_main
      return _run_code(code, main_globals, None,
    File "/Users/meirgabay/.pyenv/versions/3.8.2/Python.framework/Versions/3.8/lib/python3.8/runpy.py", line 86, in _run_code
      exec(code, run_globals)
    File "/Users/meirgabay/python-project/src/app/app.py", line 1, in <module>
      from ..utils import message
  ValueError: attempted relative import beyond top-level package
  ```

- It doesn't happen when invoking `message`, since it doesn't use relative imports

  ```bash
  meirgabay@~/python-project/src (master)$ python utils/message.py
  My Path: python-project/src/utils/message.py


  meirgabay@~/python-project/src (master)$ python -m utils.message
  My Path: python-project/src/utils/message.py
  ```

- Invoking a function from the terminal is also possible by using the `-c` flag. Surprise, it's possible to pass arguments in a more intuitive way, for example `app.main(my_arg1, my_arg2)`
  ```bash
  meirgabay@~/python-project (master)$ python -c "import src.app.app as app; app.main()"
  Insert your name: willy
  Hello willy
  ```

### What are the available command-line flags in Python?

- Read the docs - [using cmdline](https://docs.python.org/3/using/cmdline.html)
- In this tutorial, we used both `-c` and `-m` flags

### Is there a good framework for creating a Python CLI?

- Short answer - **yes! more than a few!**
- The [Click Framework](https://click.palletsprojects.com/en/7.x/) is amazing! I used it in [githubsecrets](https://github.com/unfor19/githubsecrets) and [frigga](https://github.com/unfor19/frigga)
  <br>_NOTE_: you'll discover that I have `__init__.py` files in my projects, that's a nasty old habit, I promise I will drop them, I promise
- Read more about the available Python CLI frameworks in this great blog post - [Building Beautiful Command Line Interfaces with Python](https://codeburst.io/building-beautiful-command-line-interfaces-with-python-26c7e1bb54df)

### Where can I find a well-structured Python project?

- [Django](https://github.com/django/django) - a complex Python project
- [requests](https://github.com/psf/requests) - a non-complex Python project

## Authors

Created and maintained by [Meir Gabay](https://github.com/unfor19)
