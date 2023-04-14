from ..conftest import TestClient

class TokenStorage:
    access_token = None

def test_login(client: TestClient):
    response = client.post("/login",
        json={"username": "test", "password": "test" },
        )
    assert response.status_code == 200
    TokenStorage.access_token = response.json()['access_token']


def test_average_words_length(client: TestClient):
    response = client.post("/average-words-length", 
        headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(TokenStorage.access_token)
             },
        json={"sentence": "Hi all, my name is Tom...I am originally from Brazil." },
        )
    assert response.status_code == 200
    assert response.json() == {
        "sentence": "Hi all, my name is Tom...I am originally from Brazil.",
        "average_lengths": 3.9
    }
