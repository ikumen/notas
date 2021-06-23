from datetime import datetime
from typing import List
from pydantic import validate_arguments
from backend.app.datastores import MongoCollection


class NoteService(MongoCollection):
    def __init__(self):
        super().__init__('notes')

    @validate_arguments
    def create(self, 
            user: str,
            title: str,
            content: str = None,
            ispublic: bool = False,
            tags: List[str] = None,
            **kwargs # hacky but allows us to ignore extra fields
        ) -> dict:
        """Create a note.
        """
        utc_now = datetime.utcnow()
        return super().create(user=user, title=title, content=content,
            ispublic=ispublic, tags=tags, created_at=utc_now, updated_at=utc_now)
        

note_service = NoteService()