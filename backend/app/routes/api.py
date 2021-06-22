import logging

from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.routing import Route


logger = logging.getLogger(__name__)

# Handler definitions
async def list_notas(req: Request):
    return JSONResponse(content=[])


# Handler to route mappings
uri_prefix = '/notas'

routes = [
    Route(uri_prefix, endpoint=list_notas, methods=['GET'])
]