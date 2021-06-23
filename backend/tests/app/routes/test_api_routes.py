import json

from starlette.testclient import TestClient
# fixture that returns the Starlette TestClient
# note run_around_tests depends on mongo_db_client 
from backend.tests.helper import app_client, mongo_db_client, notes_collection, run_around_tests


def test_api_list_notes_should_return_empty_list(app_client: TestClient):
    res = app_client.get('/api/notes')
    assert res.status_code == 200
    assert res.content == b'[]'

def test_api_create_note_should_create_a_note(app_client: TestClient):
    note = dict(user="ikumen", title="How to build a python app")
    
    res = app_client.post('/api/notes', data=json.dumps(note))
    created_note = json.loads(res.content.decode('utf-8'))
    
    assert res.status_code == 200
    assert created_note['title'] == note['title'] \
        and created_note['user'] == note['user']
