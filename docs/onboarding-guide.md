## Python Setup

Guide for setting up Python base projects

### Requirements

- [pyenv](https://github.com/pyenv/pyenv), at some point you may need to have multiple versions of Python running. `pyenv` helps you manage and switch between versions without really messing up your environment
- [virtualenv](https://virtualenv.pypa.io/en/latest/) (for Python 2 users), otherwise Python 3 (as of 3.3) has virtual environment support built in. Every project has dependencies, many projects will have overlapping dependencies&mdash;with different versions. You use "virtual" environments to isolate each projects dependencies from each other. 
- [pip](https://pip.pypa.io/en/stable/) is the tool for installing dependencies&mdash;convention is to store the dependencies in a file called `requirements.txt` at the root of your project. _You may already have pip installed (Python 3.4+ comes with `pip`)_.

For most Python projects, I use the following process to set up my development environment. Make sure you're at the project root directory.

### Python Version

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

### Virtual Environment

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

### Managing Dependencies

Next we use `pip` to install dependencies. `pip` and `pip freeze`, are fine for small, individual projects but it can get messy with distributed teams on heterogeneous environments. What's needed is a way to lock dependencies, other platforms solve this with lock files (e.g Node's `package-lock.json`). There are plenty of Python solutions out there, I hear good things about [Poetry](https://python-poetry.org), but I prefer keeping build tools simple. I've been using `pip-compile`, part of the `pip-tools` library, with no issues. The workflow using `pip-compile` is super simple, requiring just 2 files: 

* requirements.in   (where you keep your direct dependencies)
* requirements.txt  (compile from requirements.in, contains specific versions of direct and all transitive dependencies)

```shell
(.venv) pip install pip-tools             # (contains pip-compile)
(.venv) pip-compile requirements.in       # (generates requirements.txt)
(.venv) pip-sync requirements.txt         # install/syncs all the dependencies into our virtual env
```
_Note: both requirements.in and requirements.txt are checked in source control_

#### Layered Dependencies

If you need additional dependencies for different environments (e.g, pytest in dev/test), then you can [create layered requirements](https://github.com/jazzband/pip-tools#workflow-for-layered-requirements) to manage this requirement.

For example, in addition to the `requirements.in` above, we also need `pytest` and `requests` lib in development and testing environments. Create an `requirements-test.in` layered on top of `requirements.in` dependencies.

```shell
# requirements-test.in
-c requirements.txt
pytest
requests
```

Then compile the dev/test specific `requirements-test.in`, this will produce a `requirements-test.txt`, then `pip-sync` to install.

```shell
(.venv) pip-compile requirements-test.in
(.venv) pip-sync requirements.txt requirements-test.txt
```

Finally, make sure you have a [Python specific](https://github.com/github/gitignore/blob/master/Python.gitignore) [`.gitignore`](https://docs.github.com/en/free-pro-team@latest/github/using-git/ignoring-files) for your project.

## Backend Setup



## Frontend Setup

This guide describes the frontend [Svelte](https://svelte.dev/)/[TypeScript](https://www.typescriptlang.org/) based [single-page app](https://en.wikipedia.org/wiki/Single-page_application) in terms of the structure, development flow and build. 

### File Structure

At it's base, this is the file structure for the frontend app.

```
frontend
├── app
│   ├── App.svelte
│   └── index.ts
├── package.json
├── public
│   ├── index.html
│   └── static
│       ├── bundle.css     (auto-generated)
│       ├── bundle.js      (auto-generated)
│       ├── bundle.js.map  (auto-generated)
│       ├── favicon.ico
│       └── global.css
├── rollup.config.js
└── tsconfig.json
```

- `app` is where the application logic resides, Svelte components and TypeScript files
  - `index.ts` the main entry into the app
- `public` is where all static files and auto-generated static files will reside
  - `static` all js, css files
  - `index.html` the main container for the single-page app
- `package.json` [npm package manager](https://nodejs.org/en/knowledge/getting-started/npm/what-is-the-file-package-json/)
- `rollup.config.js` [rollup.js](https://rollupjs.org/guide/en/) module bundler (e.g, webpack)
- `tsconfig.json` Typescript [compiler configurations](https://www.typescriptlang.org/docs/handbook/tsconfig-json.html)

### Build 

Our frontend application is just an HTML page that executes some sourced in JavaScript code. Except our JavaScript code starts off as Svelte and TypeScript code, and is then transpiled (TypeScript -> JavaScript), then compiled (Svelte -> JavaScript), and the output is bundled and dependencies to into a single file (`bundle.js`). That single `bundle.js` is then source in from our `index.html`.

To build the frontend for deployment you can use:

```
npm run build --prefix frontend
```
_Note: in a production environment, we may then copy the contents of `public` and auto-generated `bundle.js` to a target as part of the deployment process._

To build and serve the frontend while in development (e.g, watch for source changes and rebuild)

```
npm run dev --prefix frontend
```

## Localized Services

The `notas` application will use [Cosmos DB (Mongo interface)](https://docs.microsoft.com/en-us/azure/cosmos-db/mongodb-introduction) as the primary storage and [Redis](https://redis.io/) as caching/index. During development, these services will be made available locally via [docker](https://docs.docker.com/compose/) images, all configured in [docker-compose.yaml](../docker-compose.yaml). 

Locally, we'll use a containerized Mongo Database vs the Cosmos DB since the latter is [only available on Windows or on Linux with limit functionality](https://docs.microsoft.com/en-us/azure/cosmos-db/local-emulator?tabs=ssl-netstd21#run-on-linux-macos). 

To start the localized Mongo Database and Redis server. 

```shell
# start all services defined in docker-compose.yaml
docker-compose up

# start mongo db
docker-compose up mongodb

# start redis
docker-compose up redis
```

On Windows and MacOS, docker compose is included in docker desktop, just run compose from the docker cli.

```shell
docker compose up
```



