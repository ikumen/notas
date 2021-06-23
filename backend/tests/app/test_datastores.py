import pytest

from pymongo.database import Database, Collection
from backend.app import datastores
from backend.tests.helper import mongo_db_client, notes_collection, run_around_tests


def test_with_supplied_database(notes_collection: Collection):
    notas_store = datastores.MongoCollection(notes_collection.name, notes_collection.database)
    assert notas_store.all() == []

def test_create_should_add_note_to_store(notes_collection: Collection):
    notes_store = datastores.MongoCollection(notes_collection.name, notes_collection.database)
    # Given empty notas collections
    assert list(notes_collection.find()) == []
    title = 'How to create a starlette, svelte note-taking app'
    # When we call create with a new doc
    notes_store.create(title=title)
    # Then it should store the newly created note in mongo collection
    assert list(notes_collection.find())[0]['title'] == title

def test_all_should_list_all_notes(notes_collection: Collection):
    # Given a list of notes that we add to mongo notes collection
    notes_collection.insert_many([{'title': f'Note {n}'} for n in range(10)])
    # When we call all using our mongostore, it should return those notes above
    notes_store = datastores.MongoCollection(notes_collection.name, notes_collection.database)
    # Then all should return all the notes added above
    notes = notes_store.all()
    assert len(notes) == 10
    for note in notes:
        assert '_id' in note and 'title' in note

def test_get_should_return_note(notes_collection: Collection):
    title = 'How to create a starlette, svelte note-taking app'
    id = notes_collection.insert_one({'title': title}).inserted_id
    notes_store = datastores.MongoCollection(notes_collection.name, notes_collection.database)
    assert notes_store.get(str(id))['title'] == title

