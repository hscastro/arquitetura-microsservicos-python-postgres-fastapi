from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_notifications():
    response = client.get("/notifications")
    assert response.status_code == 200