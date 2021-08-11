from datetime import datetime
from typing import Any, List, Optional
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
            published: bool = False,
            tags: List[str] = None,
            **kwargs # hacky but allows us to ignore extra fields
        ) -> dict:
        """Create a note.
        """
        utc_now = datetime.utcnow()
        return super().create(user=user, title=title, content=content,
            published=published, tags=tags, createdate=utc_now, updatedate=utc_now)

    @validate_arguments    
    def update(self, 
            id: str,
            user: str,
            title: str = None,
            content: str = None,
            published: bool = None,
            tags: List[str] = None, 
            **kwargs
        ) -> Optional[dict]:
        """Update note with given id. Returns the id and datetime of
        the updated note.
        """
        updatedate = datetime.utcnow()
        note = dict(id=id, user=user, updatedate=updatedate)

        if title is not None:
            note['title'] = title
        if content is not None:
            note['content'] = content
        if published is not None:
            note['published'] = published
        if tags is not None:
            note['tags'] = tags

        is_updated = super().update(**note)
        if is_updated:
            return note
        return None 


note_service = NoteService()