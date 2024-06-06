from fastapi import FastAPI
from fastapi.testclient import TestClient

from hero_api.main import app

client = TestClient(app)


def test_root_path():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello Dashboard Applications!"}


def test_hero_list():
    response = client.get("/api/hero")
    assert response.status_code == 200
    assert response.json()

def test_get_hero():
    try:
        response = client.get("/api/hero/1")
        assert response.status_code == 200
        assert response.json()
    except Exception as e:
        # print(f"Test failed with exception: {e}")
        print(f"Response status code: {response.status_code}")
        print(f"Response body: {response.text}")
        raise
    
def test_