# notas
Simple markdown note-taking app for introverts

## Quick Start

**Requirements**

* Python 3.7+, pip
* TypeScript


## Onboarding 

#### Python Project Setup

You'll need the following tools

- [pyenv](https://github.com/pyenv/pyenv), at some point you may need to have multiple versions of Python running. `pyenv` helps you manage and switch between versions without really messing up your environment
- [virtualenv](https://virtualenv.pypa.io/en/latest/) (for Python 2 users), otherwise Python 3 (as of 3.3) has virtual environment support built in. Every project has dependencies, many projects will have overlapping dependencies&mdash;with different versions. You use "virtual" environments to isolate each projects dependencies from each other. 
- [pip](https://pip.pypa.io/en/stable/) is the tool for installing dependencies&mdash;convention is to store the dependencies in a file called `requirements.txt` at the root of your project. _You may already have pip installed (Python 3.4+ comes with `pip`)_.

For most Python projects, I use the following process to set up my development environment. Make sure you're at the project root directory.

Determine the Python version you will use and switch to it via [pyenv](https://github.com/pyenv/pyenv) `shell` or add a `.python-version` at the project root for `pyenv` to pick up. Here are two examples of setting the Python version, the latter method is the one I usually use.

```bash
# Quick but only applies to current shell
pyenv shell 3.7.1
python --version
Python 3.7.1

# Applies to current directory and all sub directories (preferred method) 
echo "3.8.3" > .python-version
python --version
Python 3.8.3
```

Initialize a virtual environment (I prefer to keep this directory hidden since it's managed by virtualenv).

```bash
# if you're using Python 2
virtualenv .venv

# and Python 3 version
python -m venv .venv

# .. don't forget to activate it
source .venv/bin/activate
# your prompt will change to display the virtual environment
(.venv)
```

Next we use `pip` to install dependencies. `pip` and `pip freeze`, are fine for small, individual projects but it can get messy with distributed teams on heterogeneous environments. What's needed is a way to lock dependencies, other platforms solve this with lock files (e.g Node's `package-lock.json`). There are plenty of Python solutions out there, I hear good things about [Poetry](https://python-poetry.org), but I prefer keeping build tools simple. I've been using `pip-compile`, part of the `pip-tools` library, with no issues. The workflow using `pip-compile` is super simple, requiring just 2 files: 

* requirements.in   (where you keep your direct dependencies)
* requirements.txt  (compile from requirements.in, contains specific versions of direct and all transitive dependencies)

```shell
(.venv) pip install pip-tools             # (contains pip-compile)
(.venv) pip-compile requirements.in       # (generates requirements.txt)
(.venv) pip install -r requirements.txt   # (both requirements.in and requirements.txt are checked in source control)
```

Finally, make sure you have a [Python specific](https://github.com/github/gitignore/blob/master/Python.gitignore) [`.gitignore`](https://docs.github.com/en/free-pro-team@latest/github/using-git/ignoring-files) for your project.





## 💡 **This page is just brain dump of raw ideas, feel free to add to it** 💡

## What

* markdown based note-taking web app
* support tags
* support search of title, content, tags
* minimal editing experience (check out dev.to for example)
* edit/preview modes (maybe side by side)
* signin with OAuth (e.g openid connect)
* categories?
* (future) export/archive to github gist, dropbox, download?
* (future) think about OT (operational transformations) for colab editing

## How

**I'm putting these out there to give us some direction, something concrete to discuss. Nothing is set in stone, I'm open to suggestions** 

* Python backend (leaning toward [Starlette](https://www.starlette.io/) or Flask)
* TypeScript (and JS) frontend (leaning toward [Svelte](https://svelte.dev), maybe Vue, React)
* Azure (App Service, Functions, CosmosDB)
* Redis for an inverted index implementation for simple search

## Why

* looking for a new job soon, want to have a new project showcasing skills for tech I'm interested in working in
* start simple, maybe move on to more complicated projects together

