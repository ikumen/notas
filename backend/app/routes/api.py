import logging

from starlette.requests import Request
from starlette.routing import Route
from starlette.exceptions import HTTPException
from backend.app.services import note_service
from backend.app.support import ApiJSONResponse


logger = logging.getLogger(__name__)


def _log_exception(ex: Exception):
    logger.warn(f"Caught {type(ex).__name__}. {ex}")


# Handler definitions
async def list_notes(req: Request):
    notes = note_service.all()
    return ApiJSONResponse(content=notes)


async def create_note(req: Request):
    try:
        data = {**(await req.json()), 'user': 'foobar', 'id': None}
        note = note_service.create(**data)
        return ApiJSONResponse(content=note)
    except Exception as ex:
        _log_exception(ex)
        raise HTTPException(status_code=400)


async def update_note(req: Request):
    updated_note = None
    try:
        id = req.path_params['id']
        data = await req.json()
        updated_note = note_service.update(id=id, **data)
    except Exception as ex:
        _log_exception(ex)
        raise HTTPException(status_code=400)

    if updated_note is not None:
        return ApiJSONResponse(content=updated_note)
    raise HTTPException(status_code=404)


async def get_note(req: Request):
    note = None
    try:
        id = req.path_params['id']
        note = note_service.get(id)
    except Exception as ex:
        _log_exception(ex)
        raise HTTPException(status_code=400)

    if note is not None:
        return ApiJSONResponse(content=note)
    raise HTTPException(status_code=404)


async def delete_note(req: Request):
    is_deleted = False
    try:
        id = req.path_params['id']
        is_deleted = note_service.delete(id)
    except Exception as ex:
        _log_exception(ex)
        raise HTTPException(status_code=400)

    if is_deleted:
        return ApiJSONResponse(status_code=204)
    raise HTTPException(status_code=404)


# Handler to route mappings
uri_prefix = '/notes'
uri_with_id_prefix = uri_prefix + '/{id:str}'

routes = [
    Route(uri_prefix, endpoint=list_notes, methods=['GET']),
    Route(uri_prefix, endpoint=create_note, methods=['POST']),
    Route(uri_with_id_prefix, endpoint=get_note, methods=['GET']),
    Route(uri_with_id_prefix, endpoint=delete_note, methods=['DELETE']),
    Route(uri_with_id_prefix, endpoint=update_note, methods=['PUT']),
]