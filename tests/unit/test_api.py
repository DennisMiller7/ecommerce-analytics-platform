from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_root_endpoint():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == "E-Commerce Analytics API"

def test_docs_available():
    response = client.get("/docs")

    assert response.status_code == 200
