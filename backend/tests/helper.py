import dotenv
import pytest
import os

from pathlib import Path
from pymongo import MongoClient
from pymongo.database import Database, Collection
from starlette.testclient import TestClient
from backend import application


dotenv_path = Path(__file__).parent.parent.parent / '.env'
dotenv.load_dotenv(dotenv_path)


@pytest.fixture
def app_client():
    return TestClient(application.app)

@pytest.fixture
def mongo_db_client() -> Database:
    mongo_client = MongoClient(os.environ['MONGO_URI'])
    db = mongo_client.get_database(os.environ['MONGO_DB_NAME'])
    return db

@pytest.fixture
def notes_collection(mongo_db_client: Database) -> Collection:
    return mongo_db_client.get_collection('notes')

@pytest.fixture(autouse=True)
def run_around_tests(mongo_db_client: Database):
    # before tests
    mongo_db_client.drop_collection('notes')
    # tests
    yield

