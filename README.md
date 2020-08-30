# python-project

Python project structure - a super slim example

## Getting Started

Running the application is only possible from the root directory

- `main.py`

  ```
  meirgabay@~/python-project $ python main.py
  Inesrt your name: meir
  Hello meir


  meirgabay@~/python-project $ python -m main
  Inesrt your name: willy
  Hello willy
  ```

- `app.py`

  ```
  meirgabay@~/python-project $ python -m src.app.app
  I'm in src > app > app.py
  Inesrt your name: willy
  Hello willy

  # Relative import to utils, results in an error
  meirgabay@~/python-project $ python src/app/app.py
  Traceback (most recent call last):
  File "src/app/app.py", line 1, in <module>
    from ..utils.greet import greet
  ImportError: attempted relative import with no known parent package
  ```

- `greet.py`

  ```
  meirgabay@~/python-project $ python -m src.utils.greet
  I'm in src > utils > greet.py

  # Doesn't import anything, so no errors
  meirgabay@~/python-project $ python src/utils/greet.py
  I'm in src > utils > greet.py
  ```

## Troubleshooting

### \_\_init\_\_.py

In previous versions of Python, you had to create the `__init__.py` file in each folder that you want to import as a package. From version 3.3+ it is not required anymore - [Implicit Namespace Packages](https://www.python.org/dev/peps/pep-0420/)

### ModuleNotFoundError

Trying to invoke `main()` from `src/app/app.py` directly, will raise the following error. This shows how important it is to add `if __main__` to your code

```bash
meirgabay@~/python-project $ python -m src.app.app.main
/Users/meirgabay/.pyenv/versions/3.8.2/Python.framework/Versions/3.8/bin/python: Error while finding module specification for 'src.app.app.main' (ModuleNotFoundError: __path__ attribute not found on 'src.app.app' while trying to find 'src.app.app.main')
```

### Relative import beyond top-level package

Trying to execute a package **not** from root dir will raise the following error.

```bash
meirgabay@~/python-project/src $ python -m app.app
Traceback (most recent call last):
  File "/Users/meirgabay/.pyenv/versions/3.8.2/Python.framework/Versions/3.8/lib/python3.8/runpy.py", line 193, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "/Users/meirgabay/.pyenv/versions/3.8.2/Python.framework/Versions/3.8/lib/python3.8/runpy.py", line 86, in _run_code
    exec(code, run_globals)
  File "/Users/meirgabay/python-project/src/app/app.py", line 1, in <module>
    from ..utils.greet import greet
ValueError: attempted relative import beyond top-level package
```

It doesn't happen when you invoke `greet.py`, since it doesn't import anything

```
meirgabay@~/python-project/src $ python -m utils.greet
I'm in src > utils > greet.py
```

### pylint - Attempted relative import beyond top-level packagepylint(relative-beyond-top-level)

Yup, pylint says it's an error (VSCode extension), though flake8 is fine with it. I prefer using flake8 as my linter.
