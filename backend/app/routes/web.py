from pathlib import Path
from starlette.routing import Route
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates


templates_path = Path(__file__).parent.parent / 'templates'
static = StaticFiles(directory=templates_path / 'static')
templates = Jinja2Templates(directory=templates_path)


# Handler definitions
async def index(req):
    """Entry point for our web app (single-page app)"""
    return templates.TemplateResponse('index.html', {'request': req})


# Handler to route mappings
routes = [
    Route('/{path:path}', endpoint=index)
]