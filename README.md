# Feihong's Coconut Quickstart

## Installation

Prerequisites

```
brew install python
pip3 install jupyter
```

Install coconut and jupyter via pipenv

```
pipenv shell
pip3 install coconut jupyter
```

Install coconut kernel

    python install_coconut_kernel.py

Note: If you run `coconut --jupyter`, it will install the kernel globally instead of just inside the virtualenv.

## Commands

Open notebook in jupyter notebook

    jupyter notebook notebooks/hello.ipynb

## Links

- [How coconut kernel is installed](https://github.com/evhub/coconut/blob/master/coconut/command/command.py)
