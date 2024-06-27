from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlmodel import Session
import os
from dotenv import load_dotenv
from config import get_session
from hero_api.main import app

load_dotenv()

client = TestClient(app)

connection = os.environ.get("TEST_DATABASE")
engine = create_engine(connection)   # type: ignore
def get_session_override():
    with Session(engine) as session:
        yield session
        
app.dependency_overrides[get_session] = get_session_override

# def test_root_path():
#     response = client.get("/")
#     assert response.status_code == 200
#     assert response.json() == {"message": "Hello Dashboard Applications!"}

# def test_hero_list():
#     response = client.get("/api/hero")
#     assert response.status_code == 200
#     assert response.json()
    
# def test_get_hero():
#     try:
#         response = client.get("/api/hero/1")
#         assert response.status_code == 200
#         assert response.json()
#     except Exception as e:
#         print(f"Test failed with exception: {e}")
#         print(f"Response status code: {response.status_code}")
#         print(f"Response body: {response.text}")
#         raise
    
# def test_create_hero():
#     try:
#         response = client.post("/api/hero/create", json={"name": "Jamal", "secret_name": "Billu", "age":40, "team_id":1})
#         assert response.status_code == 200
#         assert response.json()
#     except Exception as e:
#         print(f"Test failed with exception: {e}")
#         print(f"Response status code: {response.status_code}")
#         print(f"Response body: {response.text}")
#         raise

def test_update_hero():
    try:
        response = client.patch("/api/hero/update/1", json={"name": "Bilal"})
        assert response.status_code == 200
        assert response.json()
    except Exception as e:
        print(f"Test failed with exception: {e}")
        print(f"Response status code: {response.status_code}")
        print(f"Response body: {response.text}")
        raise