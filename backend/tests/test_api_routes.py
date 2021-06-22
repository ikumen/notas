from starlette.testclient import TestClient
# fixture that returns the Starlette TestClient
from backend.tests.helper import app_client


def test_api_list_notas_should_return_empty_list(app_client: TestClient):
    res = app_client.get('/api/notas')
    assert res.status_code == 200
    assert res.content == b'[]'

