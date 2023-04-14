from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

class TokenStorage:
    access_token = None

def test_login():
    response = client.post("/login",
        json={"username": "test", "password": "test" },
        )
    assert response.status_code == 200
    TokenStorage.access_token = response.json()['access_token']

def test_user():
    response = client.get("/users",
        headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(TokenStorage.access_token)
             },
    )
    assert response.status_code == 200