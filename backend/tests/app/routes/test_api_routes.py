import json

from starlette.testclient import TestClient
from pymongo.database import Collection
# fixture that returns the Starlette TestClient
# note run_around_tests depends on mongo_db_client 
from backend.tests.helper import app_client, mongo_db_client, notes_collection, run_around_tests


def _generate_note_data():
    return dict(user="ikumen", title="How to build a python app") 


def test_api_list_notes_should_return_empty_list(app_client: TestClient):
    res = app_client.get('/api/notes')
    assert res.status_code == 200
    assert res.content == b'[]'

def test_api_list_notes_should_return_some_notes(app_client: TestClient, notes_collection: Collection):
    # given an empty notes collection
    res = app_client.get('/api/notes')
    assert len(json.loads(res.content)) == 0

    # when we add some notes
    notes = [
        dict(user="user1", title="title1"),
        dict(user="user2", title="title2"),
    ]
    notes_collection.insert_many(notes)
    assert notes_collection.count_documents({}) == 2
    # and call /api/notes
    res = app_client.get('/api/notes')
    retrieved_notes = json.loads(res.content)
    assert res.status_code == 200
    assert len(retrieved_notes) == len(notes)
    assert retrieved_notes[0]['title'] in [n['title'] for n in notes]
    assert retrieved_notes[1]['title'] in [n['title'] for n in notes]

def test_api_create_note_should_create_a_note(app_client: TestClient):
    note_data = _generate_note_data()
    res = app_client.post('/api/notes', data=json.dumps(note_data))
    created_note = json.loads(res.content.decode('utf-8'))
    
    assert res.status_code == 200
    assert created_note['title'] == note_data['title'] \
        and created_note['user'] == note_data['user']

def test_api_get_note_should_return_a_note(app_client: TestClient, notes_collection: Collection):
    note_data = _generate_note_data()
    id = notes_collection.insert_one(note_data).inserted_id
    res = app_client.get(f'/api/notes/{str(id)}')
    assert json.loads(res.content)['title'] == note_data['title']

def test_api_get_note_should_return_a_404(app_client: TestClient):
    res = app_client.get('/api/notes/000000000000000000000000')
    assert res.status_code == 404

def test_api_update_note_should_fail_with_404(app_client: TestClient):
    # Valid request data, but invalid id
    res = app_client.put('/api/notes/000000000000000000000000', data=json.dumps(_generate_note_data()))
    assert res.status_code == 404

def test_api_update_note_should_fail_with_400(app_client: TestClient):
    # invalid request data, user and title are required at min
    res = app_client.put('/api/notes/000000000000000000000000', data=json.dumps({}))
    assert res.status_code == 400



