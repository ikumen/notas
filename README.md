# Notas
Simple markdown based note-taking app for introverts.

Explain side project, collaborative effort for learning, Python, Full-stack, Azure...

Here's a very high level overview of the system architecture.
```                          
     ┌─────────────────┐        ┌───────────────────┐
     │   App Service   │     ┌─>│ Cosmos DB (Mongo) │  
     │ ┌─────────────┐ │     │  └─────────┬─────────┘
     │ │    Notas    │ │     │            │
     │ │  Starlette  │ │     │  ┌─────────V─────────┐
  ┌──┴─┴───┐     ┌───┴─┴─┐   │  │  Azure Functions  │
  │ Svelte │<───>│  API  │<──┘  └─────────┬─────────┘
  │  SPA   │     │       │<──┐            │ 
  └──┬─┬───┘     └───┬─┬─┘   │  ┌─────────V─────────┐
     │ └─────────────┘ │     └──┤     Redis Index   │
     └─────────────────┘        └───────────────────┘
``` 
* App Service runs the backend API and frontend [SPA](https://en.wikipedia.org/wiki/Single-page_application)
* Cosmos DB is where all notes are stored
* Azure Functions are triggered on create/update to tokenize and index a note to Redis
* [Redis](https://redis.io/) stores the inverted index of note, providing ability to search through the note contents

## Quick Start

### Prerequisites 

* [Python 3.7+](https://www.python.org/downloads/) 
* [pip](https://pip.pypa.io/en/stable/) for Python dependency management
* [pyenv](https://github.com/pyenv/pyenv) (optional) to manage Python versions
* [npm](https://www.npmjs.com/) for JavaScript dependency management
* [docker](https://docs.docker.com/), [docker-compose](https://docs.docker.com/compose/) for container management

### Install, Build, Start and Test

Make sure you are at the project root directory and prerequisites above are satisfied.

#### Frontend App

The frontend app can be built and served through the backend server or it can run independently. The second method is ideal for development as it supports hot rebuilding and reloading of the app.

###### Build only and serve with backend server

```shell
npm install --prefix frontend
npm run build --prefix frontend
```

The build process will generate 3 files (bundle.css, bundle.js, and bundle.js.map) to `frontend/public/static` directory. From there, the build will copy `frontend/public/static/*` to `backend/app/templates` for serving with the backend app.

###### Build and run standalone with hot reloading (development mode)

```shell
npm install --prefix frontend
npm run dev --prefix frontend
```

The frontend server will start at http://localhost:5050. All calls from the frontend app to /api will be proxied to the backend server at http://localhost:5000/api.

#### Backend App

```shell
# Create the virtualenv
python -m venv .venv

# Activate virtualenv
source .venv/bin/activate

# Install pip-tools, and dependencies
(.venv) pip install pip-tools
(.venv) pip-compile backend/requirements.in      # generates backend/requirements.txt if it didn't exists
(.venv) pip-compile backend/requirements-dev.in  # generates backend/requirements-dev.txt
(.venv) pip-sync backend/requirements.txt backend/requirements-dev.txt

# Start the server
(.venv) python -m backend.application
```

The backend server will start at http://localhost:5000

#### Running Tests

```shell
(.venv) python -m pytest backend/tests
```








