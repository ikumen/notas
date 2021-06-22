import pytest

from starlette.testclient import TestClient
from backend import application


@pytest.fixture
def app_client():
    return TestClient(application.app)
