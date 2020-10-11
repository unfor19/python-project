# python-project

Python project structure, relative imports, absolute imports, packages, and modules. Let's make it simpler.

Visit this project's [Wiki Pages](https://github.com/unfor19/python-project/wiki) (docs) to learn how it all works.

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

## Final words

I hope that this blog post helped you in understanding how to create a well-structured Python project, and if it did, then Heart, Clap, Star and share!

## Authors

Created and maintained by [Meir Gabay](https://github.com/unfor19)
