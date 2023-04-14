from ..conftest import TestClient

class TokenStorage:
    access_token = None

def test_login(client: TestClient):
    response = client.post("/login",
        json={"username": "test", "password": "test" },
        )
    assert response.status_code == 200
    TokenStorage.access_token = response.json()['access_token']


def test_matched_mismatched_words(client: TestClient):
    response = client.post("/matched-mismatched-words", 
        headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(TokenStorage.access_token)
             },
        json={"sentence1": "We are really pleased to meet you in our city",
            "sentence2": "The city was hit by a really heavy storm"},
        )
    assert response.status_code == 200
    assert response.json() == {
        "different_words": ["We", "are", "pleased", "to", "meet", "you", "in", "our", "The", "was", "hit", "by", "a", "heavy", "storm"]
,       "common_words": ["really", "city"] 
    }