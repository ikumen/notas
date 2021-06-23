import logging

from starlette.requests import Request
from starlette.routing import Route
from backend.app.services import note_service
from backend.app.support import ApiJSONResponse


logger = logging.getLogger(__name__)

# Handler definitions
async def list_notes(req: Request):
    logger.info("List all notes")
    notes = note_service.all()
    return ApiJSONResponse(content=notes)


async def create_note(req: Request):
    data = await req.json()
    logger.info(f"Create a new note: {data}")
    note = note_service.create(**data)
    return ApiJSONResponse(content=note)    


# Handler to route mappings
uri_prefix = '/notes'

routes = [
    Route(uri_prefix, endpoint=list_notes, methods=['GET']),
    Route(uri_prefix, endpoint=create_note, methods=['POST'])
]