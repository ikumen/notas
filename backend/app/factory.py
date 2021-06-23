from starlette.applications import Starlette
from starlette.routing import Mount
from backend.app import settings
from backend.app.routes import web, api


def create_app():
    app = Starlette(debug=settings.APP_DEBUG, routes=[
        Mount('/api', routes=api.routes),
        Mount('/', routes=web.routes)
    ])
    return app
