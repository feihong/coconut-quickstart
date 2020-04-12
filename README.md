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

    coconut --jupyter

Note: I suspect the way this is done might not work well if you have another virtualenv that uses coconut, but not sure yet

## Commands

Start jupyter notebook that uses Coconut kernel

    coconut --jupyter notebook

## Links

- [How coconut kernel is installed](https://github.com/evhub/coconut/blob/master/coconut/command/command.py)
