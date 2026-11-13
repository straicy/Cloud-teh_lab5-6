from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_healthcheck_status():
    response = client.get("/common/healthcheck")
    assert response.status_code == 200


def test_healthcheck_body():
    response = client.get("/common/healthcheck")
    assert response.json()["status"] == "ok"
