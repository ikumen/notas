import json
import typing

from bson import objectid
from datetime import datetime
from starlette.responses import JSONResponse


class CustomJSONEncoder(json.JSONEncoder):
    """Custom JSONEncoder that serializes an ObjectId and datetime to a string.
    """
    def default(self, o: typing.Any) -> typing.Any:
        if isinstance(o, objectid.ObjectId):
            return str(o)
        if isinstance(o, datetime):
            return o.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
        else:
            return super().default(o)

custom_jsonencoder = CustomJSONEncoder()


class ApiJSONResponse(JSONResponse):
    """Custon JSONResponse that can properly serialize objects using the
    CustomJSONEncoder, used mainly api request handlers.
    """
    def render(self, content: typing.Any) -> bytes:
        return custom_jsonencoder.encode(content).encode('utf-8')
