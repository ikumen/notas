from starlette.applications import Starlette
from starlette.routing import Mount
from backend.app.routes import web, api


def create_app():
    app = Starlette(debug=True, routes=[
        Mount('/api', routes=api.routes),
        Mount('/', routes=web.routes)
    ])
    return app
