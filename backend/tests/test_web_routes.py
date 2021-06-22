from starlette.testclient import TestClient
# fixture that returns the Starlette TestClient
from backend.tests.helper import app_client


def test_web_index_should_return_index_view(app_client: TestClient):
    res = app_client.get('/')
    assert res.status_code == 200
    assert b'Notas app' in res.content
