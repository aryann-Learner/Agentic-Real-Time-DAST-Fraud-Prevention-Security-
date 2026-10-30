from fastapi.testclient import TestClient

from target_app.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "ok"
    assert payload["service"] == "travelguard-ai"
    assert payload["version"] == "0.1.0"
