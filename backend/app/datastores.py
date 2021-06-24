from bson import json_util, objectid
from pymongo import MongoClient, database
from typing import List
from backend.app import settings


class MongoCollection:
    """Generic class wrapper around Mongo DB operations around a collection.
    """
    def __init__(self, collection_name: str, db: database.Database = None):
        self.init(collection_name, db)

    def init(self, collection_name: str, db: database.Database = None):
        """Initialize this store, with the given mongo Database or create one
        if necessary, and create a reference to the underlying collection this
        store will represent.
        """
        if db is None:
            mongo_client = MongoClient(settings.MONGO_URI)
            db = mongo_client.get_database(settings.MONGO_DB_NAME)
        self.collection = db.get_collection(collection_name)

    def create(self, **kwargs) -> dict:
        """Add the given attributes to the collection as a new document.
        """
        id = self.collection.insert_one(kwargs).inserted_id
        kwargs['_id'] = id
        return kwargs

    def update(self, id, **kwargs) -> bool:
        """Update the document in the collection with the given attributes 
        and identified by the given id. Return True if document was updated.
        """
        rv = self.collection.update_one({'_id': objectid.ObjectId(id)}, {'$set': kwargs})
        return rv.matched_count == 1

    def get(self, id: str) -> dict:
        """Return the document in the collection identified by the given id.
        """
        for rv in self.collection.find({"_id": objectid.ObjectId(id)}).limit(1):
            return rv
        return None

    def all(self) -> List[dict]:
        """Return all documents in collection.
        """
        rv = self.collection.find()
        return list(rv)

    def delete(self, id: str) -> bool:
        """Delete document in collection identified by the given id. Returns 
        True if the document was deleted.
        """
        rv = self.collection.delete_one({'_id': objectid.ObjectId(id)})
        return rv.deleted_count == 1

