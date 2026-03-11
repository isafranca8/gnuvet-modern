from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_client():

    response = client.post(
        "/clients",
        json={
            "name": "Deivid",
            "phone": "11999999999"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["name"] == "Deivid"