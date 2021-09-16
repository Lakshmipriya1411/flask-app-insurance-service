import requests


def test_index():
    response = requests.get("http://0.0.0.0:8080/")
    assert response.status_code == 200
