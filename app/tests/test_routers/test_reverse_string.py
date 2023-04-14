from ..conftest import TestClient

class TokenStorage:
    access_token = None

def test_login(client: TestClient):
    response = client.post("/login",
        json={"username": "test", "password": "test" },
        )
    assert response.status_code == 200
    TokenStorage.access_token = response.json()['access_token']

def test_reverse_string(client: TestClient):
    response = client.post("/reverse-string", 
        headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(TokenStorage.access_token)
             },
        json={"number": -231 },
        )
    assert response.status_code == 200
    assert response.json() == {
        "number": -231,
        "reverted_number": -132
    }